from django.contrib.auth.models import User
from django.db import models


class Friends(models.Model):
    user1 = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='user1')
    user2 = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, related_name='user2')
    user2_confirmation = models.BooleanField(default=False)
