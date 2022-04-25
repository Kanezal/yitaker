from django import forms
from .models import Community


class AddGroupForm(forms.Form):
    name = forms.CharField(
        label='Название',
        max_length=200,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control'
            }
        )
    )

    icon = forms.ImageField(
        label="Иконка сообщества"
    )

    creater = forms.CharField(
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

    description = forms.CharField(
        label='Описание',
        max_length=5000,
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
            }
        )
    )


