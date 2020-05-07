from django.conf import settings
from django.test import Client, RequestFactory, TestCase
from django.test.utils import override_settings
from django.urls import reverse

from .. import factories as accounts_factories


class TestUserTimeZone(TestCase):
    def setUp(self):
        self.client = Client()

    def test_default(self):
        response = self.client.get(reverse('timezone-test'))
        self.assertEqual(response.content.decode("utf-8"), "UTC")

    def test_ja(self):
        user = accounts_factories.User(timezone="Asia/Tokyo")
        self.client.force_login(user)
        response = self.client.get(reverse('timezone-test'))
        self.assertEqual(response.content.decode("utf-8"), "JST")


class TestUserLanguage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_default(self):
        user = accounts_factories.User()
        self.client.force_login(user)
        response = self.client.get(reverse('language-test'))
        self.assertEqual(
            response.content.decode("utf-8"),
            "all your base are belong to us"
        )

    def test_ja(self):
        user = accounts_factories.User(language="ja")
        self.client.force_login(user)
        response = self.client.get(reverse('language-test'))
        self.assertEqual(
            response.content.decode("utf-8"),
            "君達の基地は、全て我々がいただいた"
        )


@override_settings(USER_G11N_USERPROFILE_ATTRIBUTE_NAME="profile_attr")
class TestUserTimeZoneForProfileModel(TestCase):
    def setUp(self):
        self.client = Client()

    def test_default(self):
        response = self.client.get(reverse('timezone-test'))
        self.assertEqual(response.content.decode("utf-8"), "UTC")

    def test_ja(self):
        user = accounts_factories.User(profile_attr__timezone="Asia/Tokyo")
        self.client.force_login(user)
        response = self.client.get(reverse('timezone-test'))

        self.assertEqual(response.content.decode("utf-8"), "JST")


@override_settings(USER_G11N_USERPROFILE_ATTRIBUTE_NAME="profile_attr")
class TestUserLanguageForProfileModel(TestCase):
    def setUp(self):
        self.client = Client()

    def test_default(self):
        user = accounts_factories.User()
        self.client.force_login(user)
        response = self.client.get(reverse('language-test'))
        self.assertEqual(
            response.content.decode("utf-8"),
            "all your base are belong to us"
        )

    def test_ja(self):
        user = accounts_factories.User(profile_attr__language="ja")
        self.client.force_login(user)
        response = self.client.get(reverse('language-test'))
        self.assertEqual(
            response.content.decode("utf-8"),
            "君達の基地は、全て我々がいただいた"
        )
        self.assertNotEqual(user.language, user.profile_attr.language)
