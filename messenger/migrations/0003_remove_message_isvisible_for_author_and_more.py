# Generated by Django 4.0.3 on 2022-04-12 20:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0002_chat_message_isread_message_isvisible_all_users_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='isVisible_for_author',
        ),
        migrations.RemoveField(
            model_name='message',
            name='user_receiver',
        ),
    ]
