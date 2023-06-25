from django.contrib import admin
from django.db import transaction
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
    list_display = ('user', 'total_amount', 'total_commission', 'timestamp')
    # list_filter = ('user', 'timestamp')
    search_fields = ('user__email', 'user__first_name', 'user__last_name')
    date_hierarchy = 'timestamp'
    readonly_fields = ('total_amount', 'total_commission') 
    inlines = [TransactionDetailInline]
    
    # def save_related(self, request, form, formsets, change):
    #     with transaction.atomic():
    #         # Save the transaction details first
    #         self.save_formsets(request, form, formsets, True)

    #         # Save the transaction itself
    #         super().save_related(request, form, formsets, change)

