from django.contrib import admin
from  django.contrib.auth.admin import UserAdmin as BaseUseradmin
from apps.user.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(BaseUseradmin):
    fieldsets = (
        (None, {'fields':('username', 'password')}),
        ('Personal info', {'fields':('firts_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_activate', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )