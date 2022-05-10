# Generated by Django 4.0.4 on 2022-05-09 23:49

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0006_alter_profile_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='static\\images\\avatars\\base.png', force_format=None, keep_meta=True, quality=50, size=[500, 500], upload_to='static/images/avatars/%Y/%m/%d/'),
        ),
    ]
