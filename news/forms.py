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
    sender = forms.CharField(
        label='Пользователь',
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'disabled': '',
            }
        ),
        required=False
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
        label='Изображение'
    )
    group = forms.IntegerField(
        label='Группа',
        required=False,
    )


