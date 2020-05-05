import django
from django.utils import timezone, translation
from django.conf import settings
import pytz


class UserLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        user_language = getattr(
            request.user,
            'language',
            settings.LANGUAGE_CODE
        )
        translation.activate(user_language)

        if django.VERSION[0] <= 2:
            request.session[translation.LANGUAGE_SESSION_KEY] = user_language

        response = self.get_response(request)

        if django.VERSION[0] >= 3:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)

        return response


class UserTimeZoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            timezone.activate(pytz.timezone(request.user.timezone))
        else:
            timezone.deactivate()

        return self.get_response(request)
