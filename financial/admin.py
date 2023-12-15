from django.contrib import admin
from .models import Debt, Payment

class PaymentInline(admin.TabularInline):  # Anda dapat mengganti TabularInline dengan StackedInline sesuai preferensi tata letak
    model = Payment
    extra = 1  # Jumlah form pembayaran yang ditampilkan secara default
    # readonly_fields = ['amount', 'payment_date', 'description']  # Anda bisa menyesuaikan bidang yang ingin ditampilkan sebagai read-only

class DebtAdmin(admin.ModelAdmin):
    inlines = [PaymentInline]

admin.site.register(Debt, DebtAdmin)
