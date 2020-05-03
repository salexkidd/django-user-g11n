from django.urls import path
from user_g11n import views

urlpatterns = [
    path(
        'django_user_g11n/timezone-test',
        views.UserTimeZoneTestView.as_view(),
        name='timezone-test'
    ),

    path(
        'django_user_g11n/language-test',
        views.UserLanguageTestView.as_view(),
        name='language-test'
    ),
]