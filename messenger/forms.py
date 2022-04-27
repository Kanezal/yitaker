from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class MessageForm(forms.Form):
    text = forms.CharField(max_length = 100, label = 'Введите сообщение', widget=forms.Textarea)

class ChatForm(forms.Form):
    title = forms.CharField(max_length = 25, label = 'Чат')