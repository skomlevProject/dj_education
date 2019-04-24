from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.utils.translation import ugettext as _
from import_export.admin import ImportExportModelAdmin

from .models import *


class CustomUserAdmin(UserAdmin, ImportExportModelAdmin):

    password = ReadOnlyPasswordHashField()
    readonly_fields = ('last_login', 'date_joined', 'modified_at')
    list_display = (
        'username', 'first_name', 'last_name', 'is_active',
        'is_staff', 'is_superuser'
    )
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    fieldsets = (
        (
            _('Company'),
            {
                'fields': (
                    'company', 'office'
                )
            }
        ),
        (
            _('Personal Info.'),
            {
                'fields': (
                    'first_name', 'last_name', 'email', 'profile_image',
                    'username', 'password'
                )
            }
        ),
        (
            _('Permissions Info.'),
            {
                'classes': ('collapse',),
                'fields': (
                    'is_superuser', 'is_staff', 'is_active',
                    'user_permissions', 'groups'
                )
            }
        ),
        (
            _('Audit Info.'),
            {
                'classes': ('collapse',),
                'fields': ('last_login', 'date_joined', 'modified_at')
            }
        )
    )


admin.site.register(User, CustomUserAdmin)
