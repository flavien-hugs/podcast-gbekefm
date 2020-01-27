# cats/models.py

__author__ = 'Flavien-hugs <flavienhugs@pm.me>'
__version__= '0.0.1'
__copyright__ = '© 2019'

from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.core.files.storage import default_storage

# Create your models here.

# MODEL CATEGORIE
class Categorie(models.Model):
    CATEGORIES_CHOICES = (
        ('showbiz', 'Showbiz'),
        ('evenement', 'Evenement'),
        ('culture', 'Culture'),
        ('music', 'Music'),
        ('documentaire', 'Documentaire'),
        ('formation', 'Formation'),
        ('interview', 'Interview'),
        ('reportage', 'Reportage'),
    )
    cat = models.CharField('Categorie', max_length=50, choices=CATEGORIES_CHOICES, default='showbiz')
    slug = models.SlugField('Référence', max_length=50, unique=True, help_text='Automatiquement formé à partir du titre.')

    class Meta:
        verbose_name = 'catégorie'
        verbose_name_plural = 'catégories'
        ordering = ('cat',)

    def __str__(self):
        return self.cat

    def get_absolute_url(self):
        return reverse('cast:cat_listing', kwargs={'slug': self.slug})


# MODEL PODCAST
class Podcast(models.Model):
    categorie = models.ManyToManyField(Categorie, verbose_name="Catégorie")
    title = models.CharField('Titre', max_length=100)
    slug = models.SlugField('Url', max_length=100, unique=True, help_text="Automatiquement formé à partir du titre.")
    description = models.TextField('Description')
    image = models.ImageField('Image de description', upload_to="audio/",
        blank=True, null=True, help_text="Dimension d'image recommandé (300x306).")
    url_audio = models.URLField('Url fichier audio', max_length=200)
    publish = models.DateTimeField('Date de publication', default=timezone.now)
    like = models.IntegerField('Nombre de votes', default=0)

    class Meta:
        ordering = ('publish',)
        verbose_name = 'podcast'
        verbose_name_plural = 'podcasts'

    def __str__(self):
        return "%s (%s)" % (
            self.title, ", ".join(categorie.cat for categorie in self.categorie.all()),)

    def get_absolute_url(self):
        return reverse('cast:podcast', kwargs={'slug': self.slug, 'pk': self.id})

    def save(self):
        try:
            img = Podcast.objects.get(pk=self.id)
            path = img.image.path
            if img.image.path != self.small_image.path_1:
                default_storage.delete(path)
            elif self.remove_image:
                self.image = None
                default_storage.delete(path)
        except:
            pass
        self.remove_image = False

        super(Podcast, self).save()