# Generated by Django 4.0.4 on 2022-05-09 23:29

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0004_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=django_resized.forms.ResizedImageField(crop=['center'], default='static\\images\\avatars\\base.png', force_format=None, keep_meta=True, quality=-1, size=[500, 500], upload_to='static/images/avatars/%Y/%m/%d/'),
        ),
    ]