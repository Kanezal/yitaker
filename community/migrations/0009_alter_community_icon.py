# Generated by Django 4.0.2 on 2022-04-25 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0008_community_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='icon',
            field=models.ImageField(upload_to='static/images/community_icons/%Y/%m/%d/'),
        ),
    ]