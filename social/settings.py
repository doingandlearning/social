"""
Django settings for social project.

Generated by 'django-admin startproject' using Django 1.11.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import dj_database_url

from django.core.urlresolvers import reverse_lazy

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'enkpyb8pk9^gk8e%+kq35n0tta(k@!zzer*z=4z_8=z!dm%tfo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['http://kcshed.com', 'social-photo-bookmarking.herokuapp.com','kcshed.com', 'localhost', '127.0.0.1']
ABSOLUTE_URL_OVERRIDES ={
    'auth.user': lambda u: reverse_lazy('user_detail', args=[u.username])
}

# Application definition

INSTALLED_APPS = [
    # custom apps
    'account',
    'images',
    'actions',

    # 3rd party
    'social_django',
    'sorl.thumbnail',

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

ROOT_URLCONF = 'social.urls'

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

WSGI_APPLICATION = 'social.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'social',
        'USER': 'deployer',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '',
    }
}

db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)


# Authentication and Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

#Facebook settings
SOCIAL_AUTH_FACEBOOK_KEY = '1707059289368051'
SOCIAL_AUTH_FACEBOOK_SECRET = '5207d9dff2f3150b29d36b668f92d85b'
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_API_VERSION = '2.10'

#Google settings
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY='228762371032-j80vrqtbvn9jrrrriqnfkn3790f9ulpq.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'WNEVUBBJKRBVUixdXAwCG0mV'

#Twitter settings
SOCIAL_AUTH_TWITTER_KEY = "hObYTUoxvZMBoQkj4hEFVex0B"
SOCIAL_AUTH_TWITTER_SECRET = "fb242X43722Y5FOKIKYG0v0K7AilDiaK9MBeH4I1xIGIKoSua7"

#Git hub settings
SOCIAL_AUTH_GITHUB_KEY = '276b95f4de367aa1ca82'
SOCIAL_AUTH_GITHUB_SECRET = 'ee58cb791798cf20b7a43c826548284e63c80194'

AUTHENTICATION_BACKENDS = (
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.open_id.OpenIdAuth',
    'social_core.backends.google.GoogleOpenId',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.google.GoogleOAuth',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.github.GithubOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'account.authentication.EmailAuthBackend',
)

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

LOGGING_CONFIG = None
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'debug.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')


LOGIN_REDIRECT_URL = reverse_lazy('dashboard')
LOGIN_URL = reverse_lazy('login')
LOGOUT_URL = reverse_lazy('logout')

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Redis server settings

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0
