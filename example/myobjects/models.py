from django.db import models
from django.utils.translation import ugettext_lazy as _


class MyObject(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        help_text=_("Your Name")
    )

    birthday = models.DateTimeField(
        null=False,
        blank=False,
        help_text=_("Birth of Date")
    )
