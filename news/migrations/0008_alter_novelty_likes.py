# Generated by Django 4.0.3 on 2022-03-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_novelty_title_picture_alter_novelty_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novelty',
            name='likes',
            field=models.IntegerField(null=True),
        ),
    ]
