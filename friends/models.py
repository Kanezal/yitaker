from django.contrib.auth.models import User
from django.db import models


class Friends(models.Model):
    user1 = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user1', default=None, null=True)
    user2 = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='user2', default=None, null=True)
    user2_confirmation = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user1.username} : {self.user2.username} - {'дружба' if self.user2_confirmation else 'не дружба'}"
