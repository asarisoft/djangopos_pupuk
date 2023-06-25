from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin


class CustomUserAdmin(DjangoUserAdmin):
    list_display = ( 'mobile_number', 'full_name', 'parent',)
    autocomplete_fields = ['parent']
    search_fields = ['parent__full_name', 'full_name']
    fieldsets = (
        (None, {'fields': ('mobile_number','full_name', 'parent',  'password')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )
    add_fieldsets = (
        (None, {'fields': ('mobile_number','full_name', 'parent')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser',)}),
    )

# admin.site.register(CustomUser)
admin.site.register(CustomUser, CustomUserAdmin)  # Register the User admin with custom settings

from django.contrib.auth.models import Group
admin.site.unregister(Group)