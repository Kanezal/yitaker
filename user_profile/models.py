from django.db import models
from django_resized import ResizedImageField

from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        User,
        null=True,
        on_delete=models.CASCADE,
    )

    img = ResizedImageField(
        size=[500, 500],
        default='static\\images\\avatars\\base.png',
        upload_to='static/images/avatars/%Y/%m/%d/',
        crop=['middle', 'center'],
        quality=50,
    )

    city = models.CharField(max_length=300, null=True, blank=True)
    other_socnet = models.CharField(max_length=300, null=True, blank=True)
    career = models.CharField(max_length=300, null=True, blank=True)
    interests = models.CharField(max_length=300, null=True, blank=True)
    favorite_musics = models.CharField(max_length=300, null=True, blank=True)
    favorite_movies = models.CharField(max_length=300, null=True, blank=True)
    favorite_TVshows = models.CharField(max_length=300, null=True, blank=True)
    favorite_books = models.CharField(max_length=300, null=True, blank=True)
    favorite_games = models.CharField(max_length=300, null=True, blank=True)
    favorite_quotes = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(max_length=300, null=True, blank=True)
    about_me = models.CharField(max_length=300, null=True, blank=True)
    life_position = models.CharField(max_length=300, null=True, blank=True)
    political_preferences = models.CharField(max_length=300, null=True, blank=True)
    world_outlook = models.CharField(max_length=300, null=True, blank=True)
    main_in_life = models.CharField(max_length=300, null=True, blank=True)
    main_in_people = models.CharField(max_length=300, null=True, blank=True)
    attitude_to_smoking = models.CharField(max_length=300, null=True, blank=True)
    attitude_to_alcohol = models.CharField(max_length=300, null=True, blank=True)
    inspires = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"Профиль пользователя: {self.user}"