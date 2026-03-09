from django.contrib import admin
from .models import Member
from django.contrib.auth.admin import UserAdmin


class CustomAdmin(UserAdmin):
    model=Member
    list_display=('id','email','first_name','last_name','is_active')
    list_filter=('is_staff','is_active')
    fieldsets=(
        (None,{'fields':('email','password')}),
        ('Personal Info',{'fields':('first_name','last_name')}),
        ('Permissions',{'fields':('is_staff','is_active','is_superuser','groups','user_permissions')}),
        ('Important Dates',{'fields':('last_login','date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active'),
        }),
    )
    search_fields=('email',)
    ordering=('email',)


admin.site.register(Member,CustomAdmin)
