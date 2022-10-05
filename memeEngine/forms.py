from cProfile import label
from logging import PlaceHolder
from pdb import post_mortem
from tkinter import Widget
from django import forms
from .models import Meme
from taggit.models import Tag

#tag_choices = Tag.objects.all().values_list('name', 'name')

#tag_list = []

#for item in tag_choices:
    #tag_list.append(item)

class uploadForm(forms.ModelForm):
    class Meta:
        model = Meme
        fields = ('__all__')
        labels = {
            'image' : 'Drop The Meme',
            'name' : 'Name It',
            #'tag' : 'Tag It',
        }

        widgets = {
            'image' : forms.FileInput(attrs={'class': 'fileUpload'}),
            'name' : forms.TextInput(attrs={'class': 'formInput'}),
            #'tag' : forms.SelectMultiple(choices=tag_list, attrs={'class' : 'formInput'}),
        }