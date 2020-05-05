Django User g11n
=========================================================================================

Django supports *i18n* and *l10n*. However, there is no item to set the user's time zone and region as a default feature.

Django User g11n (*globalization*) provides fields for users to set time zones and regions, as well as middleware to handle them properly.

<img src="https://raw.githubusercontent.com/wiki/salexkidd/django-user-g11n/imgs/example.gif" width="800px">

Core idea is [See the Django documentation for more information](https://stackoverflow.com/questions/10235956/django-1-4-how-to-automatically-get-users-timezone-from-client)

- Support Django 2 and 3
- Support Python3.7, 3.8 (Maybe 2.7. Not tested)


# Usage

Install the package from pypi

```
$ pip install django-user-g11n
```

## Create a custom user model

Create an application for custom users. Please refer to the Django documentation for more information.
[See the Django documentation for more information](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/)

```
$ manage.py startapp accounts
```

Add the following to your application's models.py

```
from django.contrib.auth import models as auth_models
from user_g11n.models import UserLanguageSupportMixin, UserTimeZoneSupportMixin


class User(UserTimeZoneSupportMixin,
           UserLanguageSupportMixin,
           auth_models.AbstractUser):
    pass
```

## modifying to settings.py

### INSTALLED_APPS

Add a user-extended application and user_g11n to INSTALLED_APPS.

```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    .
    .
    .
    'accounts',  # Your Custom user model application
    'user_g11n', # Add
)
```

### MIDDLEWARE

Added two middleware provided by django_user_g11n.

```
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    .
    .
    .
    'user_g11n.middleware.UserLanguageMiddleware', # Add
    'user_g11n.middleware.UserTimeZoneMiddleware', # Add
]
```

### AUTH_USER_MODEL

Change or add the AUTH_USER_MODEL.

```
AUTH_USER_MODEL = 'accounts.User'
```

### I18N, L10N & TIME_ZONE setting

Change the I18N, L10N, and TZ settings.

```
USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = "Asia/Tokyo" # Change to your local timezone
```

## migrate

Migration to adapt the changes.

```
$ ./manage.py makemigrations
$ ./manage.py migrate
```

# Demo

The Docker configuration is provided. Please use the following command to start it. Go to [http://localhost:8000](http://localhost:8000) when the launch is complete.

```
$ docker-compose up
```
