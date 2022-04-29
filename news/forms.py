from django import forms
from .models import Novelty


class AddNoveltyForm(forms.Form):
    name_new = forms.CharField(
        label='Название',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    text = forms.CharField(
        label='Текст',
        max_length=5000,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                # 'style': 'height:500px'
            }
        )
    )

    picture = forms.ImageField(
        label='Изображение',
        required=False,
    )


