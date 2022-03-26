from django import forms
from .models import Novelty


class ImageForm(forms.ModelForm):
    class Meta:
        model = Novelty
        fields = ('name_new', 'text', 'picture')
