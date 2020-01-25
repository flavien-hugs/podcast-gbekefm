# -*- coding: utf-8 -*-

from django.urls import path

from cast.views import (
    SearchView, PodcastDetailView, PodcastAboutView,
    PodcastMonthArchiveView, uplike
    )
    
from cast.models import Podcast

app_name = 'cast'

urlpatterns = [
    path('search/', SearchView.as_view(), name='search'),
    path('p/<slug>/<pk>/', PodcastDetailView.as_view(), name='podcast'),
    path('p/<slug:slug>/<int:podcast_id>/like/', uplike, name='uplike'),
    path('p/archive/<str:month>/<int:year>/', PodcastMonthArchiveView.as_view(), name='archive_month'),
    path('about/', PodcastAboutView.as_view(), name='about'),
]
