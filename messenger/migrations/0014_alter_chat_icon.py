# Generated by Django 4.0.4 on 2022-05-17 17:37

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('messenger', '0013_remove_chat_user_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='icon',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='static/images/avatars/base.png', force_format=None, keep_meta=True, quality=50, size=[500, 500], upload_to='static/group_chat/'),
        ),
    ]
