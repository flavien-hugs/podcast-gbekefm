"""podcast URL Configuration
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from cast.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', include("cast.urls", namespace='cast')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
