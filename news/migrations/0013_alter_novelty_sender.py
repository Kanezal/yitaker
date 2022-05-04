# Generated by Django 4.0.4 on 2022-05-02 20:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0012_remove_noveltylikes_created_novelty_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novelty',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='news_reporter', to=settings.AUTH_USER_MODEL),
        ),
    ]
