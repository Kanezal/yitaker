from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MessageForm(forms.Form):
    user_sender = forms.CharField(max_length = 50, label = 'Введите свое имя')
    text = forms.CharField(max_length = 100, label = 'Введите сообщение', widget = forms.Textarea)