"""
Django settings for gcanvas project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

import os

from django.core.exceptions import ImproperlyConfigured
from unipath import Path
import dj_database_url

DATABASES = {
    "default": dj_database_url.config()
}

NATIONBUILDER_CLIENT_ID='92a6946dd65005738232de85da413892d9b714441917ccea6641427a147c6e5e'
NATIONBUILDER_CLIENT_SECRET='6e7cd58f2ec94b44f9adc1099e7f4c4ac95d9c61a5ecf55c1b7f77db3209bd72'
NATIONBUILDER_CLIENT_NAME='gCanvas'


# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

def get_env_variable(var_name):
    """get the environment variable or return exception"""
    try:
        return os.environ.get(var_name)
    except KeyError:
        error_msg = "Set the %s environment variable" % (var_name)
        raise ImproperlyConfigured(error_msg)


BASE_DIR = Path(__file__).ancestor(3)
MEDIA_ROOT = BASE_DIR.child('media')
STATIC_ROOT = BASE_DIR.child('static')
STATICFILES_DIRS = (
    BASE_DIR.child('assets'),
    BASE_DIR.child('build').child('web'),
)

TEMPLATE_DIRS = (
    BASE_DIR.child('templates'),
)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = get_env_variable("DJANGO_SECRET_KEY")

TWITTER_CLIENT_ID='lz3KLlOaekxeuRkngh0V9BdLZ'
TWITTER_CLIENT_SECRET='8AHFZo1KEfXh7v4r4SHnT67kOdSFMJAI7iHR78U6wSQBA8gmZ5'


USER_REGISTER_URL='/'

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'oauth2_provider',
    'static_server',
    'json_handler',
    'twitter_authenticate',
    'email_verification',
    'gcanvas_user',
    'nationbuilder_connect',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oauth2_provider.middleware.OAuth2TokenMiddleware',
)

ROOT_URLCONF = 'gcanvas.urls'

WSGI_APPLICATION = 'gcanvas.wsgi.application'


# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'


AUTHENTICATION_BACKENDS = (
    # ... your other backends
    'twitter_authenticate.auth_backend.TwitterAuthBackend',
)
