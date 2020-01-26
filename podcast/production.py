# -*- coding: utf-8 -*-

__author__ = 'Flavien-hugs <contact@unsta.ci>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta'

import dj_database_url
from podcast.settings import *

DEBUG = TEMPLATE_DEBUG = False

# SECURITE SSL/HTTPS
SECURE_SSL_REDIRECT = True

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# APPLICATION DEFINITION
INSTALLED_APPS += ['whitenoise.runserver_nostatic']

# 'django.middleware.security.SecurityMiddleware',
MIDDLEWARE += ['whitenoise.middleware.WhiteNoiseMiddleware']
#  Add configuration for static files storage using whitenoise

ALLOWED_HOSTS = ['gbekefm.herokuapp.com']
