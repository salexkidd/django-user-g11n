from django.utils import timezone, translation
import pytz


class UserLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            user_language = getattr(request.user, 'language', None)
            translation.activate(user_language)
            request.session[translation.LANGUAGE_SESSION_KEY] = user_language
        except Exception as e:
            pass

        return self.get_response(request)


class UserTimeZoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            timezone.activate(pytz.timezone(request.user.timezone))
        else:
            timezone.deactivate()

        return self.get_response(request)
