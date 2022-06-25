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

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-@_pq)z5#^(-1ilj-!j!&y)h+arp52ahg7)$7v&0ytjy*jydrl-'

# SECURITY WARNING: don't run with debug turned on in production!
#
# * 変更前
# DEBUG = True
# * 変更後
DEBUG = False

# * 変更前
# ALLOWED_HOSTS = []
# * 変更後
ALLOWED_HOSTS = [
    "localhost",
    "127,0,0,1",
    # --------
    # 1
    #
    # 1. 例えば レンタルサーバーを借りたときなどは、ここに IPアドレス や ホスト名 を入れないと、外部からWebサイトが見れないだろう
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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
        'DIRS': [],
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

WSGI_APPLICATION = 'project1.wsgi.application'
#                   -------------------------
#                   1
# 1. DjangoのWSGI設定の大元となるグローバル変数。
#    `host1/project1/wsgi.py` ファイルの中の application 変数を指している
#           -------------


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
