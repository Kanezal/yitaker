from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import GroupChat

users = GroupChat.all_users

class MessageForm(forms.Form):
    text = forms.CharField(max_length = 100, label = 'Введите сообщение', widget=forms.Textarea)

class ChatForm(forms.Form):
    title = forms.CharField(max_length = 25, label = 'Чат')

    users = User.objects.all()
    users_list = []
    for user in users:
        users_list.append([user.id, user.username])

    all_users = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=users_list
    )