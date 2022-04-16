from django.contrib.auth.models import User
from django.db import models


class Community(models.Model):
    name = models.CharField(max_length=50)
    creater = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=1000)
    datetime = models.DateTimeField(auto_now_add=True)


class ExistenceInGroup(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
    group = models.ForeignKey(to=Community, on_delete=models.SET_NULL, null=True)

