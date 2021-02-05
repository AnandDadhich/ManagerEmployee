"""
Django settings for Assignment project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import datetime

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_0*j+@n5f6zsik#fc9o6-hq*1$3k+$vkapwm9&lx$r$^3dv8(9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    #Applictions
    'users',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    
    #Third Party Packages
    'rest_auth',
    'rest_framework',
    'rest_framework.authtoken',
    'phone_field',
    'allauth',
    'allauth.account',
]

SITE_ID = 1
USERNAME = None
AUTH_USER_MODEL = 'users.UserInfo'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Assignment.urls'

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

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
       'rest_framework.permissions.AllowAny',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
}

WSGI_APPLICATION = 'Assignment.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

from datetime import timedelta

# JWT_AUTH = {
#     'JWT_ENCODE_HANDLER':
#         'rest_framework_jwt.utils.jwt_encode_handler',
#     'JWT_DECODE_HANDLER':
#         'rest_framework_jwt.utils.jwt_decode_handler',
#     'JWT_PAYLOAD_HANDLER':
#         'rest_framework_jwt.utils.jwt_payload_handler',
#     'JWT_PAYLOAD_GET_USER_ID_HANDLER':
#         'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',
#     'JWT_RESPONSE_PAYLOAD_HANDLER':
#         'rest_framework_jwt.utils.jwt_response_payload_handler',
#
#     'JWT_SECRET_KEY': 'SECRET_KEY',
#     'JWT_GET_USER_SECRET_KEY': None,
#     'JWT_PUBLIC_KEY': None,
#     'JWT_PRIVATE_KEY': None,
#     'JWT_ALGORITHM': 'HS256',
#     'JWT_VERIFY': True,
#     'JWT_VERIFY_EXPIRATION': True,
#     'JWT_LEEWAY': 0,
#     'JWT_EXPIRATION_DELTA': timedelta(days=30),
#     'JWT_AUDIENCE': None,
#     'JWT_ISSUER': None,
#     'JWT_ALLOW_REFRESH': False,
#     'JWT_REFRESH_EXPIRATION_DELTA': timedelta(days=30),
#     'JWT_AUTH_HEADER_PREFIX': 'Bearer',
#     'JWT_AUTH_COOKIE': None,
# }

JWT_AUTH = {
    'JWT_AUTH_HEADER_PREFIX': 'JWT',
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=300)
}