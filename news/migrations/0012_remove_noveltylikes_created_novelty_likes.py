# Generated by Django 4.0.3 on 2022-04-12 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_remove_novelty_likes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noveltylikes',
            name='created',
        ),
        migrations.AddField(
            model_name='novelty',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]