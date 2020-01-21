# -*- coding: utf-8 -*-

from django.urls import path

from cast.views import PodcastDetailView, PodcastAboutView

app_name = 'cast'

urlpatterns = [
    path('podcast/', PodcastDetailView.as_view(), name='podcast'),
    path('about/', PodcastAboutView.as_view(), name='about'),
]
