from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.contrib.auth.hashers import make_password
import factory


class User(factory.django.DjangoModelFactory):
    first_name = "testuser"

    last_name = factory.Sequence(lambda n: '{0}'.format(n))

    username = factory.Sequence(lambda n: 'testuser-{0}'.format(n))

    email = factory.Sequence(lambda n: 'testuser-{0}@example.com'.format(n))

    password = make_password("testtest")

    class Meta:
        model = get_user_model()
