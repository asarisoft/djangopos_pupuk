from django.contrib import admin
from django.utils import timezone
from .models import CashFlow

class MonthFilter(admin.SimpleListFilter):
    title = 'Month'
    parameter_name = 'month'

    def lookups(self, request, model_admin):
        months = [
            (i, timezone.datetime(2023, i, 1).strftime('%B')) for i in range(1, 13)
        ]
        return months

    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(date__month=self.value())
        
class CashFlowAdmin(admin.ModelAdmin):
    list_filter = [MonthFilter]  # Add the custom month filter

admin.site.register(CashFlow, CashFlowAdmin)