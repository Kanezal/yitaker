# Generated by Django 4.0.3 on 2022-04-23 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0006_existenceingroup_is_existed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='existenceingroup',
            name='is_existed',
        ),
    ]
