from django.contrib.auth.models import User
from django.db import models

class Community(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True)
