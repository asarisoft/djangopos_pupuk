from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'default_commission', 'commission_percentage')
    # fields = ('name', 'price')
    # readonly_fields = ('price',)  # Contoh field yang hanya dapat dibaca (readonly)
    # search_fields = ('name',)

    # def get_readonly_fields(self, request, obj=None):
    #     if obj:  # Ubah readonly field jika objek sudah ada (misalnya saat mengedit)
    #         return self.readonly_fields + ('name',)
    #     return self.readonly_fields

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['default_commission'].help_text = 'Komisi dari pupuk jika customer datang sendiri.'
        form.base_fields['commission_percentage'].help_text = 'Komisi dari pupuk untuk customer referensi dari agen.'
        return form

admin.site.register(Product, ProductAdmin)