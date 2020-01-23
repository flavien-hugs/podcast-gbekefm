# cast/templatetags/tags.py

from django import template
from ..models import Categorie, Podcast

register = template.Library()

#AFFICHER LES 03 DERNIERS PODCASTS

@register.inclusion_tag('cast/podcast_latest.html')
def latest_podcast(count=3):
    latest = Podcast.objects.filter(publish__isnull=False).order_by('-publish')[:count]
    context = { 'latest': latest }
    return context