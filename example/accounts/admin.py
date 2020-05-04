from django.contrib import admin

from . import models as accounts_models


class CustomUserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "email",
        "language",
        "timezone",
        "last_login",
    )


admin.site.register(accounts_models.User, CustomUserAdmin)
