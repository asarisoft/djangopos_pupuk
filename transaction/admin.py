from django.contrib import admin
from django.db import transaction
from django.contrib.humanize.templatetags import humanize
from .models import Transaction, TransactionDetail
from django import forms

class TransactionDetailForm(forms.ModelForm):
    class Meta:
        model = TransactionDetail
        fields = '__all__'
        readonly_fields = ('price', 'profit', 'commission_percentage', 'commission')  # Fields to be made read-only

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.Meta.readonly_fields:
            self.fields[field].widget.attrs['readonly'] = True
            self.fields[field].widget.attrs['disabled'] = True

class TransactionDetailInline(admin.TabularInline):
    model = TransactionDetail
    form = TransactionDetailForm
    extra = 0

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'formatted_total_amount', 'formatted_total_commission', 'timestamp', 'is_debt_paid', 'remaining_debt')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    date_hierarchy = 'timestamp'
    readonly_fields = ('formatted_total_amount', 'formatted_total_commission') 
    inlines = [TransactionDetailInline]

    def formatted_total_amount(self, obj):
        return humanize.intcomma(obj.total_amount)

    formatted_total_amount.admin_order_field = 'total_amount'  # Make it sortable in Django Admin

    def formatted_total_commission(self, obj):
        return humanize.intcomma(obj.total_commission)

    formatted_total_commission.admin_order_field = 'total_commission'  # Make it sortable in Django Admin

    def is_debt_paid(self, obj):
        return obj.debt.is_paid

    is_debt_paid.short_description = 'Debt Paid'
    is_debt_paid.boolean = True  # Display as a boolean (checkmark or cross)

    def remaining_debt(self, obj):
        return humanize.intcomma(obj.debt.remaining_amount)

    remaining_debt.short_description = 'Remaining Debt'

    def get_queryset(self, request):
        # Optimize queryset to fetch related debt data
        return super().get_queryset(request).select_related('debt')

    # class Media:
    #     js = ('pupuk/admin.js',)
