from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from friends.models import Friends
from .models import Message
from django.db.models import Q

class MessageForm(forms.ModelForm):
    text = forms.CharField(label = 'Введите сообщение', widget=forms.Textarea)
    class Meta:
        model = Message
        fields = ('text', )
        widgets = {
            'text': forms.Textarea()
        }

class ChatForm(forms.Form):
    title = forms.CharField(max_length = 25, label = 'Чат')

    option = forms.MultipleChoiceField(
        choices = [],
        widget = forms.CheckboxSelectMultiple()
    )

    def __init__(self, *args, **kwargs):
        id = kwargs.pop('id')
        super(ChatForm, self).__init__(*args, **kwargs)

        user = User.objects.get(id=id)
        
        friends_Q = Friends.objects.filter(
            (Q(user1=user) | Q(user2=user)) & Q(user2_confirmation=True)
        )
        friends_my = User.objects.none()
        for friends in friends_Q:
            if friends.user1 != user:
                friends_my = friends_my | User.objects.filter(id = friends.user1.id)
            else:
                friends_my = friends_my | User.objects.filter(id = friends.user2.id)

        my_friends = []
        for el in friends_my:
            my_friends.append([el.id, el.username])
            
        self.fields["option"].choices = my_friends
        
    
        