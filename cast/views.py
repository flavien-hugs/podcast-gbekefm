# -*- coding: utf-8 -*-

from django.urls import reverse
from django.db.models import Q, F
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.dates import MonthArchiveView
from django.http import HttpResponse, HttpResponseRedirect

from cast.models import Podcast, Categorie


# VUE DE RECHERCHE
class SearchView(View):

    def get(self, request, *args, **kwargs):
        queryset = Podcast.objects.all()
        query = request.GET.get('q')
        if query:
            queryset = queryset.filter(
                Q(title__icontains=query) | Q(description__icontains=query) |
                Q(categorie__cat__icontains=query)).distinct()

        context = {'queryset': queryset}
        template = 'cast/podscat_search.html'
        return render(request, template, context)



# VUE DE LA PAGE D'ACCUEIL
class HomeView(ListView):

    model = Podcast
    template_name = 'index.html'

    def get_queryset(self):
        return Podcast.objects.order_by('publish')[:10]

    def head(self, *args, **kwargs):
        latest_podcast = self.get_queryset().latest('publish')
        response = HttpResponse('')
        response['Last-Modified'] = latest_podcast.publish.strftime('%a, %d %b %Y %H:%M:%S GMT')
        return response

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        cat = Categorie.objects.all()
        context['categorie'] = cat

        return context


# VUE DE LA PAGE DE DETAIL
class PodcastDetailView(DetailView):

    model = Podcast
    template_name = 'cast/podcast_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PodcastDetailView, self).get_context_data(**kwargs)
        cat = Categorie.objects.all()
        context['categorie'] = cat

        return context


# VUE LIKE PODCAST
def uplike(request, slug, podcast_id):
    if request.method == 'POST':
        podcast = get_object_or_404(Podcast, slug=slug, pk=podcast_id)
        podcast.like += 1
        podcast.save()
        return HttpResponseRedirect(reverse('cast:podcast',
            args=[podcast.slug, podcast.id]))


# VUE DE LA PAGE ABOUT
class PodcastAboutView(TemplateView):
	template_name = 'cast/podcast_about.html'

	def get_context_data(self, **kwargs):
	    context = super(PodcastAboutView, self).get_context_data(**kwargs)
	    context['title'] = "about".upper()
	    return context


# VUE ARCHIVE DU MOIS
class PodcastMonthArchiveView(MonthArchiveView):
    queryset = Podcast.objects.dates('publish', 'month')
    date_field = "publish"
    month_format = '%m'
    year_format = '%Y'
    allow_future = False	