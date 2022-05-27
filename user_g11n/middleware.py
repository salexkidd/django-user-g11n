import django

from .utils import can_use_pytz

if can_use_pytz():
    import pytz
else:
    import zoneinfo

from django.conf import settings
from django.utils import timezone, translation


class UserLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_anonymous:
            user_language = settings.LANGUAGE_CODE
        elif getattr(settings, "USER_G11N_USERPROFILE_ATTRIBUTE_NAME", None):
            profile = getattr(
                request.user,
                settings.USER_G11N_USERPROFILE_ATTRIBUTE_NAME,
            )
            user_language = getattr(profile, "language")
        else:
            user_language = getattr(
                request.user,
                "language",
                settings.LANGUAGE_CODE
            )

        translation.activate(user_language)
        response = self.get_response(request)

        if django.VERSION[0] <= 2:
            request.session[translation.LANGUAGE_SESSION_KEY] = user_language

        if django.VERSION[0] >= 3:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

        return response


class UserTimeZoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_anonymous:
            timezone.deactivate()
        else:
            if getattr(settings, "USER_G11N_USERPROFILE_ATTRIBUTE_NAME", None):
                profile = getattr(
                    request.user, settings.USER_G11N_USERPROFILE_ATTRIBUTE_NAME)
                user_tz = getattr(profile, "timezone")
            else:
                user_tz = getattr(request.user, "timezone")

            if can_use_pytz():
                timezone.activate(pytz.timezone(user_tz))
            else:
                timezone.activate(zoneinfo.ZoneInfo(user_tz))

        return self.get_response(request)
