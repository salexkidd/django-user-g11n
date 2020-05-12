from django.conf import settings
from django.test import TestCase
from django.test.utils import override_settings

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
