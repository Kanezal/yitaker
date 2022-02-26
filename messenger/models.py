from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Message(models.Model):
    user_sender = models.ForeignKey(to = settings.AUTH_USER_MODEL, on_delete = models.SET_NULL, null=True, related_name = 'sender')
    user_receiver = models.ForeignKey(to = User, on_delete = models.SET_NULL, null=True, related_name = 'receiver')
    text = models.TextField()
    date_receipt = models.DateTimeField()
    