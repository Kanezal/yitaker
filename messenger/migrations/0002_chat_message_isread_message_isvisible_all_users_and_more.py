from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('messenger', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=25)),
                ('icons', models.FileField(upload_to='')),
                ('date_of_creation', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='isRead',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='message',
            name='isVisible_all_users',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='message',
            name='isVisible_for_author',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='date_receipt',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.CreateModel(
            name='Chat_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='messenger.chat')),
                ('user_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='chat_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='messenger.chat'),
        ),
    ]
