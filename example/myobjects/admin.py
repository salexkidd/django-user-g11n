from django.contrib import admin

from . import models as myobjects_models


@admin.register(myobjects_models.MyObject)
class MyObject(admin.ModelAdmin):
    list_display = (
        "name",
        "birthday",
    )
