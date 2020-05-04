
Django User g11n
=========================================================================================

Djangoは *i18n* 及び *l10n* に対応しています。しかし、デフォルトの機能としてユーザーのタイムゾーン及び地域を設定する項目は存在しません。

Django User g11n(i18n + l10n = globalization)は、ユーザーにタイムゾーンと地域を設定するためのフィールドと、それらを適切に扱うためのミドルウェアを提供します。


# インストール方法

pypiからパッケージをインストールします

```
$ pip install django-user-g11n
```

## ユーザーモデルを拡張する

ユーザー拡張用のアプリケーションを作成します。名前は

```
$ manage.py startapp accounts
```

作成したアプリケーションのmodels.pyに以下を追記します。

```python
from django.contrib.auth import models as auth_models
from user_g11n.models import UserLanguageSupportMixin, UserTimeZoneSupportMixin


class User(UserTimeZoneSupportMixin,
           UserLanguageSupportMixin,
           auth_models.AbstractUser):
    pass
```

## settings.py の変更

### INSTALLED_APPSへ追加

INSTALLED_APPSにユーザー拡張を施したアプリケーションと、user_g11n を追加します。

```python
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    .
    .
    .
    'accounts',  # <= ユーザー拡張用のモデルを含んだアプリケーション
    'user_g11n', # <= 追加
)
```

### MIDDLEWAREへ追加

MIDDLEWARE(またはMIDDLEWARE_CLASSES)にミドルウェアを追加します。

```python
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
    'user_g11n.middleware.UserLanguageMiddleware', # <= 追加
    'user_g11n.middleware.UserTimeZoneMiddleware', # <= 追加
]
```

### AUTH_USER_MODELの変更

以下をsettings.pyに追記します

```python
AUTH_USER_MODEL = 'accounts.User'
```

### I18N, L10N & TIME_ZONEの設定

以下をsettings.py追加します(既に追加されている可能性もあります)

```python
USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = "Asia/Tokyo" # あなたのシステムのデフォルトタイムゾーン

```