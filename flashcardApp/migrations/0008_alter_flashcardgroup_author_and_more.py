# Generated by Django 4.2.7 on 2023-12-21 20:40

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flashcardApp', '0007_alter_flashcardgroup_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcardgroup',
            name='author',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='flashcardgroup',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 21, 21, 40, 52, 684619)),
        ),
    ]
