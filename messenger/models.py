from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Message(models.Model):
    user_sender = models.ForeignKey(to = settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null=True, related_name = 'sender')
    user_receiver = models.ForeignKey(to = User, on_delete = models.SET_NULL, null=True, related_name = 'receiver')
    text = models.TextField()
    date_receipt = models.DateTimeField()
    chat_id = models.ManyToManyField(to = Chat) # id Диалога к которому относится сообщение
    isRead = models # прочитано ли сообщение получателем
    isVisible_only_for_author = models# видимость сообщение для первого юзера
    isVisible_all_users = models# видимость сообщение для первого юзера (для возможности отчисти сообщений, если просто удалять тогда сообщение пропадет из истории у обоих юзеров)

class Chat:
    title = models.CharField(max_length= 25)# заголовок чата, его название
    creator = models.ForeignKey(to = User, on_delete=models.CASCADE)# id пользователя создавшего чат
    icon = models.ImageField(null=True, blank=True, upload_to="images/") # иконка чата
    date_of_creation = models.DateTimeField() # время создания

class Chat_user(models.Model):
    chat_id = models.ForeignKey(to = Chat, on_delete = models.SET_NULL)
    user_id = models.ForeignKey(to = User, on_delete = models.SET_NULL)