from django.db import models


class Novelty(models.Model):
    user_id = models.IntegerField()
    wall_id = models.IntegerField()
    text = models.CharField(max_length=3000)
    pictures = models.FileField()
    likes = models.IntegerField()
