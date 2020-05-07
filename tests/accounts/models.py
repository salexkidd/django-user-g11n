import pytz
from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.translation import ugettext_lazy as _

from user_g11n.models import UserLanguageSupportMixin, UserTimeZoneSupportMixin


class User(UserTimeZoneSupportMixin,
           UserLanguageSupportMixin,
           auth_models.AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile_attr",
    )

    timezone = models.CharField(
        db_index=True,
        max_length=100,
        choices=[(t, t) for t in pytz.common_timezones],
        default="UTC",
        null=False,
        blank=False,
        verbose_name=_("TimeZone")
    )

    language = models.CharField(
        max_length=10,
        choices=settings.LANGUAGES,
        default=settings.LANGUAGE_CODE,
        verbose_name=_("Language")
    )
