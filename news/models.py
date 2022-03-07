from django.db import models


class Novelty(models.Model):
    user_id = models.IntegerField()
    wall_id = models.IntegerField()
    text = models.CharField(max_length=3000)
    picture = models.ImageField()
    likes = models.IntegerField()
    datetime = models.DateTimeField(auto_now_add=True)
