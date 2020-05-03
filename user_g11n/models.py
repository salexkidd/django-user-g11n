"""
TimeZone and Language Mixin Classes
"""
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

import pytz

__all__ = (
    "UserTimeZoneSupportMixin",
    "UserLanguageSupportMixin",
    "TimeZoneAndUserLanguageSupportMixin",
)


class UserTimeZoneSupportMixin(models.Model):
    """ TimeZone Support """
    timezone = models.CharField(
        db_index=True,
        max_length=100,
        choices=[(t, t) for t in pytz.common_timezones],
        default="UTC",
        null=False,
        blank=False,
        verbose_name=_("TimeZone")
    )

    class Meta:
        abstract = True


class UserLanguageSupportMixin(models.Model):
    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
        verbose_name=_("Language")
    )

    class Meta:
        abstract = True


class TimeZoneAndUserLanguageSupportMixin(UserTimeZoneSupportMixin,
                                          UserLanguageSupportMixin):
    class Meta:
        abstract = True
