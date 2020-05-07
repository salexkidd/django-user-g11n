from django.contrib.auth import models as auth_models
from django.db import models

from user_g11n.models import UserLanguageSupportMixin, UserTimeZoneSupportMixin


class User(UserTimeZoneSupportMixin,
           UserLanguageSupportMixin,
           auth_models.AbstractUser):

    profile = models.OneToOneField(
        "Profile",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )


class Profile(UserTimeZoneSupportMixin,
              UserLanguageSupportMixin,
              models.Model):
    pass
