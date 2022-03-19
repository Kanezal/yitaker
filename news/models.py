from django.contrib.auth.models import User
from django.db import models

from community.models import Community


class Novelty(models.Model):
    sender = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(to=Community, on_delete=models.SET_NULL, null=True)
    name_new = models.CharField(max_length=100)
    text = models.CharField(max_length=3000)
    picture = models.FileField()
    likes = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
