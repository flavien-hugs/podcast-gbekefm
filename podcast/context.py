# insta/context.py
# -*- coding: utf-8 -*-

__author__ = 'Flavien-hugs <flavienhgs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019 unsta'

# CONTEXTE PROCESSORS CONFIGURATION

from podcast import settings

def podcast(request):
	return {
		'author': "Gbêkê Fm",
		'site_name': settings.SITE_NAME,
		'site_description': settings.SITE_DESCRIPTION,
		'meta_keywords': settings.META_KEYWORDS,
		'request': request
	}
