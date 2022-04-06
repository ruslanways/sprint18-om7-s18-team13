from re import M
from django import forms
from .models import *

class AddBook(forms.Form):
    name = forms.CharField(max_length=128)
    description = forms.CharField(max_length=128)
    count = forms.IntegerField()
    authors = forms.ModelChoiceField(queryset=Author.objects.all())
    myfield = forms.BooleanField()
    slug = forms.SlugField(max_length=20)
    mail = forms.EmailField()

