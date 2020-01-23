from django.contrib import admin

from cast.models import Categorie, Podcast

# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_filter = ('cat',)
    prepopulated_fields = {
        'slug': ('cat',)
    }

@admin.register(Podcast)
class PodcastAdmin(admin.ModelAdmin):
    list_filter = ('categorie',)
    prepopulated_fields = {
        'slug': ('title',)
    }
