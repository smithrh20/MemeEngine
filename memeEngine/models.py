from django.contrib import admin
from pyexpat import model
from unicodedata import name
from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse
from taggit.managers import TaggableManager

class Meme (models.Model):
    image = models.ImageField(upload_to='images/') 
    name = models.CharField(max_length=50)
    tag = TaggableManager()
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detailView', args=(str(self.id)) )

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url