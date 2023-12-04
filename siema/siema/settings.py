"""
Django settings for siema project.

Generated by 'django-admin startproject' using Django 4.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv


# Load variables from the .env file
load_dotenv()

db_name = os.environ.get('DBNAME')
db_user = os.environ.get('DBUSER')
db_password = os.environ.get('DBPASSWORD')
db_host = os.environ.get('DBHOST')
secret_key = os.environ.get('SECRET_KEY')
debug = os.environ.get('DEBUG', False) == 'True'
recaptcha_private_key_checkbox = os.environ.get('RECAPTCHA_PRIVATE_KEY_CHECKBOX')
recaptcha_public_key_checkbox = os.environ.get('RECAPTCHA_PUBLIC_KEY_CHECKBOX')
recaptcha_private_key_invisible = os.environ.get('RECAPTCHA_PRIVATE_KEY_INVISIBLE')
recaptcha_public_key_invisible = os.environ.get('RECAPTCHA_PUBLIC_KEY_INVISIBLE')

MAINTENANCE_MODE = os.environ.get('MAINTENANCE_MODE')
MAINTENANCE_END_TIME = os.environ.get('MAINTENANCE_END_TIME')

# MAINTENANCE_MODE = False
# MAINTENANCE_END_TIME = None  # Format: 'YYYY-MM-DD HH:MM:SS'

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = secret_key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = debug

ALLOWED_HOSTS = ['127.0.0.1', '.vercel.app', 'localhost']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'siemablog',
    'akun',
    'feedback',
    'analytic',
    'captcha',
]

MIDDLEWARE = [
    'siemablog.middleware.maintenance_middleware.MaintenanceMiddleware',
    'analytic.middleware.AnalyticsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'siema.urls'

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

WSGI_APPLICATION = 'siema.wsgi.app'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': db_name,
        'USER': db_user,
        'PASSWORD': db_password,
        'HOST': db_host,
        'PORT': '5432',
        'OPTIONS': {'sslmode': 'require'},
    }
}


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.postgresql",
#         "NAME": "verceldb",
#         "USER": "default",
#         "PASSWORD": "H0i6PCQtYwRh",
#         "HOST": "ep-red-smoke-30854751-pooler.us-east-1.postgres.vercel-storage.com",
#         "PORT": "5432",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = 'id'
TIME_ZONE = 'Asia/Singapore'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# STATIC_ROOT = BASE_DIR / "static/"
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_DIRS = os.path.join(BASE_DIR, "static"),
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles_build', 'static')

# STORAGES = {
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/akun/login/'
LOGIN_REDIRECT_URL = '/dashboard'
LOGOUT_REDIRECT_URL = '/akun/logout'

MESSAGE_STORAGE = 'django.contrib.messages.storage.fallback.FallbackStorage'

AUTH_PASSWORD_VALIDATORS = []

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_NAME = 'sesi_pengguna'

# RECAPTCHA_PUBLIC_KEY_CHECKBOX = recaptcha_public_key_checkbox
# RECAPTCHA_PRIVATE_KEY_CHECKBOX = recaptcha_private_key_checkbox
RECAPTCHA_PUBLIC_KEY = recaptcha_public_key_invisible
RECAPTCHA_PRIVATE_KEY = recaptcha_private_key_invisible

# SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
