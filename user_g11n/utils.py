import django
from django.conf import settings


def can_use_pytz():
    return django.VERSION[0] <= 3 or (django.VERSION[0] >= 4 and getattr(settings, "USE_DEPRECATED_PYTZ"))
