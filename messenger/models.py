from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

from django_resized import ResizedImageField

class Chat(models.Model):

    title = models.CharField(max_length=255, null=True)# заголовок чата, его название
    icon = ResizedImageField(
        size=[500, 500],
        default='images/avatars/base.png',
        upload_to='static/tmp/',
        crop=['middle', 'center'],
        quality=50,
    )
    
    user1 = models.ForeignKey(User, related_name='chat_user1', on_delete=models.PROTECT, null=True)
    user2 = models.ForeignKey(User, related_name='chat_user2', on_delete=models.PROTECT, null=True)

    date_of_creation = models.DateTimeField(auto_now_add = True) # время создания


class GroupChat(models.Model):
    title = models.CharField(max_length = 25)# заголовок чата, его название
    user_creator = models.ForeignKey(to = User, on_delete = models.SET_NULL, null=True)# id пользователя создавшего чат
    icon = ResizedImageField(
        size=[500, 500],
        default='images\\avatars\\base.png',
        upload_to='images/avatars/%Y/%m/%d/',
        crop=['middle', 'center'],
        quality=50,
    )
    date_of_creation = models.DateTimeField(auto_now_add = True) # время создания

class Message(models.Model):
    user_sender = models.ForeignKey(to = settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null = True, related_name = 'sender')
    text = models.TextField()
    date_receipt = models.DateTimeField(auto_now_add=True) #посмотреть параметр
    chat_id = models.ForeignKey(to = Chat, on_delete = models.CASCADE, null=True) # id Диалога к которому относится сообщение
    isRead = models.BooleanField(default = False)
    isVisible_all_users = models.BooleanField(default = True)
  
class ChatUser(models.Model):
    chat_id = models.ForeignKey(to = Chat, on_delete = models.CASCADE, null=True, related_name="chatuser")
    user_id = models.ForeignKey(to = User, on_delete = models.CASCADE, null=True)