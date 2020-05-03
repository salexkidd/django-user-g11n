from django.contrib.auth import models as auth_models
from django.db import models
from django.utils.translation import ugettext_lazy as _

from user_g11n.models import UserLanguageSupportMixin, UserTimeZoneSupportMixin


class User(UserTimeZoneSupportMixin,
           UserLanguageSupportMixin,
           auth_models.AbstractUser):
    pass
