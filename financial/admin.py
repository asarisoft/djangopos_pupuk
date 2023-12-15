from django.contrib import admin
from django import forms
from django.db import models
from .models import Debt, Payment


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
        }

class PaymentInline(admin.TabularInline):  
    model = Payment
    form = PaymentForm
    extra = 1  

class DebtAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]
    readonly_fields = ('amount', 'amount_paid', 'remaining_amount')
    search_fields = ['customer__full_name']
    list_filter = ['is_paid']

    formfield_overrides = {
        models.TextField: {'widget': forms.Textarea(attrs={'rows': 4, 'cols': 40})},
    }

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

admin.site.register(Debt, DebtAdmin)
