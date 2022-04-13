from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Chat(models.Model):
    title = models.CharField(max_length = 25)# заголовок чата, его название
    creator = models.ForeignKey(to = User, on_delete = models.SET_NULL, null=True)# id пользователя создавшего чат
    icons = models.FileField() # иконка чата
    date_of_creation = models.DateTimeField(auto_now_add = True) # время создания

class Message(models.Model):
    user_sender = models.ForeignKey(to = settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null = True, related_name = 'sender')
    text = models.TextField()
    date_receipt = models.DateTimeField(auto_now_add=True) #посмотреть параметр
    chat_id = models.ForeignKey(to = Chat, on_delete = models.SET_NULL, null = True) # id Диалога к которому относится сообщение
    isRead = models.BooleanField(default = False)
    isVisible_all_users = models.BooleanField(default = True)
class Group_Message:
    pass
class Group_Chat:
    title = models.CharField(max_length = 25)# заголовок чата, его название
    icons = models.FileField() # иконка чата
    date_of_creation = models.DateTimeField(auto_now_add = True) # время создания
class Chat_user(models.Model):
    chat_id = models.ForeignKey(to = Chat, on_delete = models.SET_NULL, null=True)
    user_id = models.ForeignKey(to = User, on_delete = models.SET_NULL, null=True)
