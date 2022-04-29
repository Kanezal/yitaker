from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import GroupChat

users = GroupChat.all_users

class MessageForm(forms.Form):
    text = forms.CharField(max_length = 100, label = 'Введите сообщение', widget=forms.Textarea)

class ChatForm(forms.Form):
    title = forms.CharField(max_length = 25, label = 'Чат')
    all_users = forms.ChoiceField(choices=((1, "English"), (2, "German"), (3, "French")))