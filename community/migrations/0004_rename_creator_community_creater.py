# Generated by Django 4.0.3 on 2022-04-13 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0003_community_datetime'),
    ]

    operations = [
        migrations.RenameField(
            model_name='community',
            old_name='creator',
            new_name='creater',
        ),
    ]
