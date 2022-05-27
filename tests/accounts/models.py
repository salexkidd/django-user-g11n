from django.conf import settings
from django.contrib.auth import models as auth_models
from django.db import models

try:
    from django.utils.translation import ugettext_lazy as _
except ImportError as e:
    from django.utils.translation import gettext_lazy as _


from user_g11n.models import UserLanguageSupportMixin, UserTimeZoneSupportMixin


class User(UserTimeZoneSupportMixin,
           UserLanguageSupportMixin,
           auth_models.AbstractUser):
    pass


class UserProfile(UserTimeZoneSupportMixin,
                  UserLanguageSupportMixin,
                  models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile_attr",
    )
