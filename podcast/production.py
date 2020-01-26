# -*- coding: utf-8 -*-

__author__ = 'Flavien-hugs <contact@unsta.ci>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta'

import dj_database_url
from podcast.settings import *

DEBUG = False

# SECURITE SSL/HTTPS
SECURE_SSL_REDIRECT = True

# Parse database configuration from $DATABASE_URL
DATABASES['default'] = dj_database_url.config()

# 'django.middleware.security.SecurityMiddleware',

#  Add configuration for static files storage using whitenoise

ALLOWED_HOSTS = ['gbekefm.herokuapp.com']
