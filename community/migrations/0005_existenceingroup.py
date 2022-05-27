# Generated by Django 4.0.3 on 2022-04-13 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('community', '0004_rename_creator_community_creater'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExistenceInGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='community.community')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
