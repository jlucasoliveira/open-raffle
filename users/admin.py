from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):
    search_fields = ("name", "username")
    list_filter = ("is_active", "is_staff")
    list_display = (
        "username",
        "name",
    )
    readonly_fields = ("date_joined",)
    add_fieldsets = ((None, {"fields": ("name", "username", "password1", "password2")}),)
    fieldsets = (
        (None, {"fields": ("username", "name", "password")}),
        (
            "Permissões",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Datas Importantes", {"fields": ("last_login", "date_joined")}),
    )
    filter_horizontal = UserAdmin.filter_horizontal
