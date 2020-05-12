Django User g11n
=========================================================================================

[![CircleCI](https://circleci.com/gh/salexkidd/django-user-g11n/tree/master.svg?style=svg)](https://circleci.com/gh/salexkidd/django-user-g11n/tree/master)

Djangoは *i18n* 及び *l10n* に対応しています。しかし、デフォルトの機能としてユーザーのタイムゾーン及び地域を設定する項目は存在しません。

Django User g11n (*globalization*)は、ユーザーにタイムゾーンと地域を設定するためのフィールドと、それらを適切に扱うためのミドルウェアを提供します。

<img src="https://raw.githubusercontent.com/wiki/salexkidd/django-user-g11n/imgs/example.gif" width="800px">

根底のアイディアは以下のURLを参照してください。

[See the Django documentation for more information](https://stackoverflow.com/questions/10235956/django-1-4-how-to-automatically-get-users-timezone-from-client)

- Support Django 2 and 3
- Support Python3.7, 3.8 (Maybe 2.7. Not tested)

# インストール方法

pypiからパッケージをインストールします

```shell
$ pip install django-user-g11n
```

次に実装方法を以下の2つから選択します。

- プロファイルモデルを利用している場合
- カスタムユーザーモデルを利用している場合

プロファイルモデルはDjangoのユーザーモデルと *OneToOneField* で結びついている、ユーザーにまつわる情報を扱うモデルを指します。もし、既にこの方式で実装を勧めている場合は *プロファイルモデルを利用している場合* を参照してください。

カスタムユーザーモデルは、Djangoのユーザーモデルそのものを拡張してデータをもたせる方法です。ユーザーをカスタムモデルを利用するためにはアプリケーションを作成し、モデルをカスタマイズします。[詳細はDjangoのドキュメントを参照してください](https://docs.djangoproject.com/en/3.0/topics/auth/customizing/)

## プロファイルモデルを利用する場合

プロファイルモデルを扱うアプリケーションを作成します。

```
$ manage.py startapp accounts

作成したアプリケーションのmodels.pyに以下を追記します。

```python
from django.db import models
from user_g11n.models import UserLanguageSupportMixin, UserTimeZoneSupportMixin


class UserProfile(UserTimeZoneSupportMixin,
                  UserLanguageSupportMixin,
                  models.Model):

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="profile",
    )
```


## カスタムユーザーモデルを利用する場合

Djangoはカスタムユーザーモデルを用意し、Django標準のものを拡張することが可能です。

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

## settings.py

### INSTALLED_APPS

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

### MIDDLEWARE

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

AUTH_USER_MODELを変更または追加します。

```python
AUTH_USER_MODEL = 'accounts.User'
```

### I18N, L10N & TIME_ZONEの設定

I18N, L10N, TZの設定を変更します。

```python
USE_I18N = True

USE_L10N = True

USE_TZ = True

TIME_ZONE = "Asia/Tokyo" # Change to your local timezone
```

## プロファイルモデルを利用している場合(プロファイルアトリビュートの指定)

ユーザーモデルに紐付いたプロファイルモデルのアトリビュート名を設定します。

```
USER_G11N_USERPROFILE_ATTRIBUTE_NAME = "profile"
```

もしプロファイルモデルで指定したユーザーモデルへのOneToOneField中にて、related_nameが "foobar" になっていれば、ここの値を以下のようにします。

```
USER_G11N_USERPROFILE_ATTRIBUTE_NAME = "foobar"
```



## migrate

Migrationを行い変更を適応します。

```
$ ./manage.py migrate
```

# Demo

Dockerの設定を用意しています。以下のコマンドを用いて起動してください。起動が完了したら [http://localhost:8000](http://localhost:8000) にアクセスしてください。

```
$ docker-compose up
```

