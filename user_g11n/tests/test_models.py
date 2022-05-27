import django
from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings, skipUnless

try:
    from django.utils.translation import ugettext_lazy as _
except ImportError as e:
    from django.utils.translation import gettext_lazy as _

from ..utils import can_use_pytz


from .. import factories as accounts_factories


class TestUserLanguage(TestCase):
    def test_default_user_language(self):
        user = accounts_factories.User()
        self.assertEqual(user.language, settings.LANGUAGE_CODE)

    def test_change_user_language(self):
        user = accounts_factories.User()
        user.language = "ja"
        user.save()
        user.refresh_from_db()

        self.assertEqual(user.language, "ja")


class TestUserTimeZone(TestCase):
    def test_default_user_language(self):
        user = accounts_factories.User()
        self.assertEqual(user.language, settings.LANGUAGE_CODE)

    def test_change_user_language(self):
        user = accounts_factories.User()
        user.timezone = "Asia/Tokyo"
        user.save()

        self.assertEqual(user.timezone, "Asia/Tokyo")


@override_settings(USER_G11N_USERPROFILE_ATTRIBUTE_NAME="profile_attr")
class TestUserLanguageForProfileModel(TestCase):
    def test_change_user_language(self):
        user = accounts_factories.User()

        profile = getattr(user, "profile_attr")
        profile.language = "ja"
        profile.save()

        self.assertEqual(user.profile_attr.language, "ja")
        self.assertNotEqual(user.language, user.profile_attr.language)


@override_settings(USER_G11N_USERPROFILE_ATTRIBUTE_NAME="profile_attr")
class TestUserTimeZoneForProfileModel(TestCase):
    def test_change_user_language(self):
        user = accounts_factories.User()

        profile = getattr(user, "profile_attr")
        profile.timezone = "Asia/Tokyo"
        profile.save()
        profile.refresh_from_db()

        self.assertEqual(user.profile_attr.timezone, "Asia/Tokyo")
        self.assertNotEqual(user.timezone, user.profile_attr.timezone)


class TestUtils(TestCase):
    @skipUnless(django.VERSION[0]<=3, "This test django4 only")
    def test_can_use_pytz_django_3(self):
        self.assertTrue(can_use_pytz())
        import pytz

    @skipUnless(django.VERSION[0] >= 4, "This test django4 only")
    def test_can_use_pytz_django_4(self):
        self.assertFalse(can_use_pytz())

    @override_settings(USE_DEPRECATED_PYTZ=True)
    @skipUnless(django.VERSION[0] >= 4, "This test django4 only")
    def test_can_use_pytz_django_4_if_use_reprecated_pytz_is_true(self):
        self.assertTrue(can_use_pytz())


