# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.views.generic.detail import DetailView

# VUE DE LA PAGE D'ACCUEIL
class HomeView(TemplateView):
	"""docstring for HomeListView"""
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
	    context = super(HomeView, self).get_context_data(**kwargs)
	    context['title'] = "accueil".upper()
	    return context


# VUE DE LA PAGE DE DETAIL
class PodcastDetailView(TemplateView):
	"""docstring for PodcastDetailView"""
	template_name = 'cast/podcast_detail.html'


# VUE DE LA PAGE ABOUT
class PodcastAboutView(TemplateView):
	"""docstring for PodcastDetailView"""
	template_name = 'cast/podcast_about.html'

	def get_context_data(self, **kwargs):
	    context = super(PodcastAboutView, self).get_context_data(**kwargs)
	    context['title'] = "about".upper()
	    return context
		