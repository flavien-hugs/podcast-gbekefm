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

# MIDDLEWARE_CLASSES
MIDDLEWARE_CLASSES += ["djangosecure.middleware.SecurityMiddleware"]

# HTTP STRICT TRANSPORT SECURITY
SECURE_HSTS_SECONDS = 5OO
SECURE_HSTS_INCLUDE_SUBDOMAINS = True

# PROTECTION CONTRE LE DETOURNEMENT DE CLICS
SECURE_FRAME_DENY = True

# FILTRAGE XSS DU NAVIGATEUR
SECURE_BROWSER_XSS_FILTER = True

# 'django.middleware.security.SecurityMiddleware',

#  Add configuration for static files storage using whitenoise

ALLOWED_HOSTS = ['gbekefm.herokuapp.com']
