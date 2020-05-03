from django.views.generic import TemplateView
from django.utils import timezone


class UserTimeZoneTestView(TemplateView):
    template_name = 'user_g11n/user_timezone.html'

    def get_context_data(self, *args, **kwargs):
        return {"datetime": timezone.now()}


class UserLanguageTestView(TemplateView):
    template_name = 'user_g11n/user_language.html'
