# Generated by Django 4.0.4 on 2022-05-27 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0016_alter_community_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='icon',
            field=models.ImageField(default='images/community_icons/no_img.png', upload_to='images/community_icons/%Y/%m/%d/'),
        ),
    ]
