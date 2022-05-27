"""
TimeZone and Language Mixin Classes
"""
import django

from .utils import can_use_pytz

if can_use_pytz():
    import pytz
    __AVAILABLE_TIMEZONE__ = [(t, t) for t in pytz.common_timezones]
else:
    import zoneinfo
    __AVAILABLE_TIMEZONE__ = [(t, t) for t in zoneinfo.available_timezones()]

from django.conf import settings
from django.db import models

try:
    from django.utils.translation import ugettext_lazy as _
except ImportError as e:
    from django.utils.translation import gettext_lazy as _



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
        choices=__AVAILABLE_TIMEZONE__,
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
