from django.conf import settings
from django.test import TestCase

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
        user.refresh_from_db()

        self.assertEqual(user.timezone, "Asia/Tokyo")
