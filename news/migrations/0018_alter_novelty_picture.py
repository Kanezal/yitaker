# Generated by Django 4.0.4 on 2022-05-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0017_alter_novelty_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novelty',
            name='picture',
            field=models.ImageField(blank=True, upload_to='static/images/novelty/%Y/%m/%d/'),
        ),
    ]
