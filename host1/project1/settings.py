"""
Django settings for project1 project.

Generated by 'django-admin startproject' using Django 3.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
from .settings_secrets import SECRET_KEY, ALLOWED_HOSTS
#    -----------------        -------------------------
#    1
# 1. `host1/project1/settings_secrets.py` を指しています
#                    ----------------
# 2. このファイル内では使われていませんが、このファイルを使う側から使われます

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
#                        ------------------------
#                        1
# 1. 例えば `host1/project1/settings.py` ファイルから見て
#    .resolve()               は `code/project1/settings.py` （`host1` は見えず `code` に差し変わっている）
#    .resolve().parent        は `code/project1/`
#    .resolve().parent.parent は `code/`
#    となっていて、つまり BASE_DIR は あなたの開発用ディレクトリーを指している


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = [
    # あなたが追加したアプリケーション
    'apps1.allauth_customized',
    'apps1.portal',
    'apps1.practice',

    # Djangoの標準アプリケーション
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # ユーザー認証のためのアプリケーション
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    # For web socket
    'channels',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project1.urls'
#               -------------
#               1
# 1. DjangoのURL設定の大元となるPythonモジュール。
#    `host1/project1/urls.py` を指している
#           -------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # * 変更前
        # 'DIRS': [],
        # * 変更後
        'DIRS': [
            os.path.join(BASE_DIR, 'apps1/practice/templates'),
            #            --------   ------------------------
            #            1          2
            #
            # Example: /host1/apps1/practice/templates/practice/v0o0o1/page1.html
            #          ------ ------------------------
            #          1      2
            #
            # 1. あなたの開発用ディレクトリー相当
            # 2. テンプレートへのパス


            # * 追加
            os.path.join(BASE_DIR, 'apps1/portal/templates'),
            #            --------   ----------------------
            #            1          2
            #
            # Example: /host1/apps1/portal/templates/portal/v0o0o1/portal_base.html
            #          ------ ----------------------
            #          1      2
            #
            # 1. あなたの開発用ディレクトリー相当
            # 2. テンプレートへのパス


            # allauth
            os.path.join(BASE_DIR, 'apps1/allauth_customized/templates'),
            #            --------   ----------------------------------
            #            1          2
            #
            # Example: /host1/apps1/allauth_customized/templates/account/signup.html
            #          ------ ----------------------------------
            #          1      2
            #
            # 1. あなたの開発用ディレクトリー相当
            # 2. テンプレートへのパス
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# * WSGI を ASGI にバージョンアップする
# ├── * 変更前
# │ WSGI_APPLICATION = 'project1.wsgi.application'
# │                     -------------------------
# │                     1
# │ 1. DjangoのWSGI設定の大元となるグローバル変数。
# │    `host1/project1/wsgi.py` ファイルの中の application 変数を指している
# │           -------------
# │
# └── * 変更後
ASGI_APPLICATION = "project1.asgi.application"
#                   -------------------------
#                   1
# 1. DjangoのASGI設定の大元となるグローバル変数。
#    `host1/project1/asgi.py` ファイルの中の application 変数を指している
#           -------------

# See also: 📖 [Django Channels and WebSockets](https://blog.logrocket.com/django-channels-and-websockets/)
CHANNEL_LAYERS = {
    'default': {
        # * Method 1: Via redis lab
        # 'BACKEND': 'channels_redis.core.RedisChannelLayer',
        # 'CONFIG': {
        #     "hosts": [
        #       'redis://h:<password>;@<redis Endpoint>:<port>'
        #     ],
        # },

        # * Method 2: Via local Redis
        # 'BACKEND': 'channels_redis.core.RedisChannelLayer',
        # 'CONFIG': {
        #      "hosts": [('127.0.0.1', 6379)],
        # },

        # Method 3: Via In-memory channel layer
        # Using this method.
        "BACKEND": "channels.layers.InMemoryChannelLayer"
    },
}


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

# * 変更前
# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }
# * 変更後
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': 'db',
        'PORT': 5432,
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# +----
# | Allauth
# |
# https://sinyblog.com/django/django-allauth/

SITE_ID = 1  # 動かしているサイトを識別するID
LOGIN_REDIRECT_URL = 'home'  # ログイン後に遷移するURL, または name の指定
LOGIN_URL = 'login'  # ログインしていないときに飛ばされる先のURL, または name の指定

# ログアウト後に遷移するURL, または name の指定
# ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/v1/login/'
#                                -------------------
#                                1
# 1. 例えば `http://example.com/accounts/v1/login/` というURLのパスの部分
#                             -------------------
ACCOUNT_LOGOUT_REDIRECT_URL = 'home'

EMAIL_HOST = 'smtp.gmail.com'  # メールサーバの指定
EMAIL_PORT = 587  # ポート番号の指定
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')  # メールサーバのGmailのアドレス
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')  # メールサーバのGmailのパスワード
EMAIL_USE_TLS = True  # TLSの設定（TRUE,FALSE)
# |
# | Allauth
# +----
