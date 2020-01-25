# -*- coding: utf-8 -*-

__author__ = 'Flavien-hugs <contact@unsta.ci>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta'

import dj_database_url
from podcast.settings import *

DEBUG = False

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

INSTALLED_APPS += ['whitenoise.runserver_nostatic']

# 'django.middleware.security.SecurityMiddleware',
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']

#  Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ALLOWED_HOSTS = ['gbekefm.herokuapp.com']
