

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import secret_keys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lolzin',
)


MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'mysite.urls'

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

#WSGI_APPLICATION = 'mysite.wsgi.application'

SECRET_KEY = os.environ["API_KEY"]

DEBUG = True

ALLOWED_HOSTS = ['*']

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


###################################
###     AWS S3 BUCKET           ###
###################################
#AWS_STORAGE_BUCKET_NAME = secret_keys.AWS_STORAGE_BUCKET_NAME
#AWS_ACCESS_KEY_ID = secret_keys.AWS_ACCESS_KEY_ID
#AWS_SECRET_ACCESS_KEY = secret_keys.AWS_SECRET_ACCESS_KEY
#AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
#STATICFILES_STORAGE = 'custom_storages.StaticStorage'
#STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, STATICFILES_LOCATION) 
MEDIAFILES_LOCATION = ''
#MEDIA_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)
MEDIA_URL = '/'
#DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
#AWS_HEADERS = {  # see http://developer.yahoo.com/performance/rules.html#expires
#    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',
#    'Cache-Control': 'max-age=94608000',
#}
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(PROJECT_ROOT, 'static'),
)

STATIC_URL = '/static/'
STATIC_ROOT='static'
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

########################################
###         BANCO DE DADOS           ###
########################################
DATABASES = {
            
        # 'default': {
        #     'ENGINE': 'django.db.backends.sqlite3',
        #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        # },
        } 
#         'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#         'NAME': 'dd81t233j9esee',                      # Or path to database file if using sqlite3.
#         # The following settings are not used with sqlite3:
#         'USER': 'teeermbjlkggzr',
#         'PASSWORD': 'VsTSljeQpO01PzjXyYn8WIvgQv',
#         'HOST': 'ec2-54-163-240-97.compute-1.amazonaws.com',# Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
#         'PORT': '5432',                      # Set to empty string for default.
#     }

#     }

import dj_database_url
DATABASES['default'] = dj_database_url.config(default=os.environ["DATABASE_URL"])


########################################
###               LOG                ###
########################################

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'mysite.log',
            'formatter': 'simple'
        },
        'file_aws': {
            'level' :   'DEBUG',
            'class' :   'logging.FileHandler',
            #'filename'  :   '/opt/python/log/lolzin.log',
            'filename'  :   'lolzin.log',
            'formatter' :    'simple'
        }
    },
    'loggers': {
        'django': {
            'handlers':['file'],
            'propagate': True,
            'level':'DEBUG',
        },
        'lolzin': {
            'handlers': ['file_aws'],
            'level': 'DEBUG',
            'propagate':    True
        },
    }
}

