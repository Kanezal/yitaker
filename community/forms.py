from django import forms
from .models import Community


class AddGroupForm(forms.Form):
    name = forms.CharField(
        label='Название',
        max_length=200,
        widget=forms.TextInput()
    )

    icon = forms.ImageField(
        label="Иконка сообщества",
        required=False,
    )

    description = forms.CharField(
        label='Описание',
        max_length=5000,
        widget=forms.Textarea()
    )
