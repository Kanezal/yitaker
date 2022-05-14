# Generated by Django 4.0.4 on 2022-05-14 00:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messenger', '0006_remove_chat_icons_remove_chat_user_creator'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='title',
        ),
        migrations.AddField(
            model_name='chat',
            name='user_1',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_user_1', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='chat',
            name='user_2',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='chat_user_2', to=settings.AUTH_USER_MODEL),
        ),
    ]
