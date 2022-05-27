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
        default='images/avatars/base.png',
        upload_to='images/avatars/%Y/%m/%d/',
        crop=['middle', 'center'],
        quality=50,
    )
    rating = models.IntegerField(default=0)
    img_confirmation = models.BooleanField(default=False)

    GENDER_CHOICES = (
        ('М', 'Мужской'),
        ('Ж', 'Женский'),
        ('Л', 'Любой'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True, verbose_name="Пол")
    birthday = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    city = models.CharField(max_length=300, null=True, blank=True, verbose_name="Город")
    other_socnet = models.CharField(max_length=300, null=True, blank=True, verbose_name="Другие соцсети")
    career = models.CharField(max_length=300, null=True, blank=True, verbose_name="Деятельность")
    interests = models.CharField(max_length=300, null=True, blank=True, verbose_name="Интересы")
    favorite_musics = models.CharField(max_length=300, null=True, blank=True, verbose_name="Любимая музыка")
    favorite_movies = models.CharField(max_length=300, null=True, blank=True, verbose_name="Любимые фильмы")
    favorite_TVshows = models.CharField(max_length=300, null=True, blank=True, verbose_name="Любимые шоу")
    favorite_books = models.CharField(max_length=300, null=True, blank=True, verbose_name="Любимые книги")
    favorite_games = models.CharField(max_length=300, null=True, blank=True, verbose_name="Любимые игры")
    favorite_quotes = models.CharField(max_length=300, null=True, blank=True, verbose_name="Любимые цитаты")
    status = models.CharField(max_length=300, null=True, blank=True, verbose_name="Статус")
    about_me = models.CharField(max_length=300, null=True, blank=True, verbose_name="Обо мне")
    life_position = models.CharField(max_length=300, null=True, blank=True, verbose_name="Жизненная позиция")
    political_preferences = models.CharField(max_length=300, null=True, blank=True, verbose_name="Политические предпочтения")
    world_outlook = models.CharField(max_length=300, null=True, blank=True, verbose_name="Мировозрение")
    main_in_life = models.CharField(max_length=300, null=True, blank=True, verbose_name="Главное в жизни")
    main_in_people = models.CharField(max_length=300, null=True, blank=True, verbose_name="Главное в людях")
    attitude_to_smoking = models.CharField(max_length=300, null=True, blank=True, verbose_name="Отношение к алкоголю")
    attitude_to_alcohol = models.CharField(max_length=300, null=True, blank=True, verbose_name="Отношение к курению")
    inspires = models.CharField(max_length=300, null=True, blank=True, verbose_name="Вдохновляют")

    def __str__(self):
        return f"Профиль пользователя: {self.user}"
