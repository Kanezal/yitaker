from django.contrib.auth.models import User
from django.db import models

from community.models import Community


class Novelty(models.Model):
    sender = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name="news")
    group = models.ForeignKey(to=Community, on_delete=models.SET_NULL, null=True)
    name_new = models.CharField(max_length=100)
    text = models.CharField(max_length=3000)
    picture = models.ImageField(upload_to='static/images/novelty/%Y/%m/%d/', blank=True)
    datetime = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

class NoveltyLikes(models.Model):
    novelty = models.ForeignKey(to=Novelty, on_delete=models.SET_NULL, null=True)
    liked_by = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    like = models.BooleanField('like', default=False)
