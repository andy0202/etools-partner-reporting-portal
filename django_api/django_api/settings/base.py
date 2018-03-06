"""
Django settings for django_api project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
import sys

import datetime

from cryptography.hazmat.backends import default_backend
from cryptography.x509 import load_pem_x509_certificate

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APPS_DIR = os.path.join(BASE_DIR, 'apps/')
sys.path.append(APPS_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
IS_TEST = False
IS_DEV = False
IS_STAGING = False
IS_PROD = False

# Get the ENV setting.
ENV = os.getenv('ENV')
if not ENV:
    raise Exception('Environment variable ENV is required!')

DATA_VOLUME = '/data'

UPLOADS_DIR_NAME = 'uploads'
MEDIA_URL = '/%s/' % UPLOADS_DIR_NAME

FILE_UPLOAD_MAX_MEMORY_SIZE = 4194304  # 4mb
MEDIA_ROOT = os.path.join(DATA_VOLUME, '%s' % UPLOADS_DIR_NAME)
STATIC_ROOT = '%s/staticserve' % DATA_VOLUME
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# Sendgrid stuff
EMAIL_BACKEND = DOMAIN_NAME = os.getenv('DOMAIN_NAME')

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'no-reply@etools.unicef.org'

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'elasticapm.contrib.django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',
    'drfpasswordless',
    'django_filters',
    'djcelery',
    'leaflet',
    'suit',
    'easy_pdf',
    'django_cron',
    'fixture_magic',

    'account',
    'cluster',
    'core',
    'indicator',
    'partner',
    'unicef',
    'ocha',
]

MIDDLEWARE_CLASSES = [
    'elasticapm.contrib.django.middleware.TracingMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    'etools.unicef.org',
    'etools-demo.unicef.org',
    'etools-test.unicef.org',
    'etools-staging.unicef.org',
    'etools-dev.unicef.org'
)

ROOT_URLCONF = 'django_api.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
              'django.template.loaders.filesystem.Loader',
              'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]

FIXTURE_DIRS = [
    '/code/fixtures/',
]

WSGI_APPLICATION = 'django_api.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': '%s' % os.getenv('POSTGRES_DB'),
        'USER': '%s' % os.getenv('POSTGRES_USER'),
        'PASSWORD': '%s' % os.getenv('POSTGRES_PASSWORD'),
        'HOST': '%s' % os.getenv('POSTGRES_HOST'),
        'PORT': 5432,
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

# JWT
# django-rest-framework-jwt: http://getblimp.github.io/django-rest-framework-jwt/
JWT_AUTH = {
   'JWT_ENCODE_HANDLER':
   'rest_framework_jwt.utils.jwt_encode_handler',

   'JWT_DECODE_HANDLER':
   'rest_framework_jwt.utils.jwt_decode_handler',

   'JWT_PAYLOAD_HANDLER':
   'rest_framework_jwt.utils.jwt_payload_handler',

   'JWT_PAYLOAD_GET_USER_ID_HANDLER':
   'rest_framework_jwt.utils.jwt_get_user_id_from_payload_handler',

   'JWT_PAYLOAD_GET_USERNAME_HANDLER':
   'rest_framework_jwt.utils.jwt_get_username_from_payload_handler',

   'JWT_RESPONSE_PAYLOAD_HANDLER':
   'rest_framework_jwt.utils.jwt_response_payload_handler',

   'JWT_ALGORITHM': 'HS256',
   'JWT_VERIFY': True,
   'JWT_VERIFY_EXPIRATION': True,
   'JWT_LEEWAY': 30,
   'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=30000),
   'JWT_AUDIENCE': None,
   'JWT_ISSUER': None,

   'JWT_ALLOW_REFRESH': False,
   'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=7),

   'JWT_AUTH_HEADER_PREFIX': 'JWT',
}
DISABLE_JWT_AUTH = os.getenv('DISABLE_JWT_AUTH', False)
# This user will be used for all externals that have a valid JWT but no user account in the system
DEFAULT_UNICEF_USER = 'default_unicef_user'
# Allows login for users that do not have a User account in the system, without creating a user account by using default
JWT_ALLOW_NON_EXISTENT_USERS = True

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/api/static/'
# FORCE_SCRIPT_NAME = '/api/'

# Authentication settings
AUTH_USER_MODEL = 'account.User'

PRINT_DATA_FORMAT = "%d-%b-%Y"
DATE_FORMAT = PRINT_DATA_FORMAT

INPUT_DATA_FORMAT = "%Y-%m-%d"

LOGS_PATH = os.path.join(DATA_VOLUME, 'django_api', 'logs')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
        'json': {
            '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
            'fmt': '%(levelname)s %(asctime)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout,
            'formatter': 'standard',
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOGS_PATH, 'django.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard'
        },
        'elasticapm': {
            'level': 'ERROR',
            'class': 'elasticapm.contrib.django.handlers.LoggingHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'INFO',
            'propagate': True
        },
        'ocha-sync': {
            'handlers': ['default', 'console'],
            'level': 'DEBUG',
            'propagate': True
        },
        'elasticapm.errors': {
            'level': 'ERROR',
            'handlers': ['default'],
            'propagate': False,
        },
    }
}

import djcelery
djcelery.setup_loader()
BROKER_URL = os.getenv('REDIS_URL', 'redis://redis:6379/0')
BROKER_VISIBILITY_VAR = os.environ.get('CELERY_VISIBILITY_TIMEOUT', 1800)
BROKER_TRANSPORT_OPTIONS = {
    'visibility_timeout': int(BROKER_VISIBILITY_VAR)}  # 5 hours

CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# Sensible settings for celery
CELERY_ALWAYS_EAGER = False
CELERY_ACKS_LATE = True
CELERY_TASK_PUBLISH_RETRY = True
CELERY_DISABLE_RATE_LIMITS = False

# By default we will ignore result
# If you want to see results and try out tasks interactively, change it to False
# Or change this setting on tasks level
CELERY_IGNORE_RESULT = True
CELERY_SEND_TASK_ERROR_EMAILS = False
CELERY_TASK_RESULT_EXPIRES = 600

# Don't use pickle as serializer, json is much safer
# CELERY_TASK_SERIALIZER = "json"
# CELERY_ACCEPT_CONTENT = ['application/json']

# CELERYD_HIJACK_ROOT_LOGGER = False
CELERYD_PREFETCH_MULTIPLIER = 1
# CELERYD_MAX_TASKS_PER_CHILD = 1000

LEAFLET_CONFIG = {
    'TILES': 'http://server.arcgisonline.com/ArcGIS/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}',
    'ATTRIBUTION_PREFIX': 'Tiles &copy; Esri &mdash; Source: Esri, DeLorme, NAVTEQ, USGS, Intermap, iPC, NRCAN, Esri Japan, METI, Esri China (Hong Kong), Esri (Thailand), TomTom, 2012',
    'MIN_ZOOM': 3,
    'MAX_ZOOM': 18,
}

# CartoDB settings
CARTODB_USERNAME = os.getenv('CARTODB_USERNAME')
CARTODB_APIKEY = os.getenv('CARTODB_APIKEY')


# Cronjobs

CRON_CLASSES = [
    'indicator.cron.IndicatorReportOverDueCronJob',
    'core.cron.WorkspaceCronJob',
    'partner.cron.PartnerCronJob',
    'unicef.cron.ProgrammeDocumentCronJob'
]

# DRF settings
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES':
        (
            'rest_framework.authentication.SessionAuthentication',
            'utils.mixins.CustomJSONWebTokenAuthentication',
            'rest_framework.authentication.TokenAuthentication',
    ),
    'DATE_FORMAT': PRINT_DATA_FORMAT,
    'DATE_INPUT_FORMATS': ['iso-8601', PRINT_DATA_FORMAT],
}


# Auth related settings
PASSWORDLESS_AUTH = {
    'PASSWORDLESS_AUTH_TYPES': ['EMAIL', ],
    'PASSWORDLESS_EMAIL_TOKEN_HTML_TEMPLATE_NAME': "account/passwordless_login_email.html",
    'PASSWORDLESS_EMAIL_NOREPLY_ADDRESS': 'no-reply@unicef.org',
    'PASSWORDLESS_CONTEXT_PROCESSORS': ['account.context_processors.passwordless_token_email', ],
    'PASSWORDLESS_REGISTER_NEW_USERS': False,
    'PASSWORDLESS_EMAIL_SUBJECT': 'UNICEF Partner Reporting Portal: Your login link'
}

# PMP API
PMP_API_ENDPOINT = "https://etools-demo.unicef.org/api"
PMP_API_USER = os.getenv('PMP_API_USER')
PMP_API_PASSWORD = os.getenv('PMP_API_PASSWORD')

# assuming we're using Azure Storage:
# django-storages: https://django-storages.readthedocs.io/en/latest/backends/azure.html
AZURE_ACCOUNT_NAME = os.environ.get('AZURE_ACCOUNT_NAME', None)  # noqa: F405
AZURE_ACCOUNT_KEY = os.environ.get('AZURE_ACCOUNT_KEY', None)  # noqa: F405
AZURE_CONTAINER = os.environ.get('AZURE_CONTAINER', None)  # noqa: F405
AZURE_SSL = True
AZURE_AUTO_SIGN = True  # flag for automatically signing urls
AZURE_ACCESS_POLICY_EXPIRY = 120  # length of time before signature expires in seconds
AZURE_ACCESS_POLICY_PERMISSION = 'r'  # read permission

if all([AZURE_ACCOUNT_NAME, AZURE_ACCOUNT_KEY, AZURE_CONTAINER]):
    DEFAULT_FILE_STORAGE = 'storages.backends.azure_storage.AzureStorage'
    from storages.backends.azure_storage import AzureStorage
    storage = AzureStorage()
    with storage.open('keys/jwt/certificate.pem') as jwt_cert:
        with open('keys/jwt/certificate.pem', 'w+') as new_jwt_cert:
            new_jwt_cert.write(jwt_cert.read())

# JWT Authentication
# production overrides for django-rest-framework-jwt
if not DISABLE_JWT_AUTH:
    public_key_text = open(os.path.join(BASE_DIR, 'keys/jwt/certificate.pem'), 'rb').read()  # noqa: F405
    certificate = load_pem_x509_certificate(public_key_text, default_backend())

    JWT_PUBLIC_KEY = certificate.public_key()

    JWT_AUTH.update({  # noqa: F405
        'JWT_SECRET_KEY': SECRET_KEY,
        'JWT_PUBLIC_KEY': JWT_PUBLIC_KEY,
        'JWT_ALGORITHM': 'RS256',
        'JWT_LEEWAY': 60,
        'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3000),  # noqa: F405
        'JWT_AUDIENCE': 'https://etools.unicef.org/',
    })

# apm related - it's enough to set those as env variables, here just for documentation
# by default logging and apm is off, so below envs needs to be set per environment

# ELASTIC_APM_SERVICE_NAME=<app-name> # set app name visible on dashboard
# ELASTIC_APM_SECRET_TOKEN=<app-token> #secret token - needs to be exact same as on apm-server
# ELASTIC_APM_SERVER_URL=http://elastic.tivixlabs.com:8200 # apm-server url

