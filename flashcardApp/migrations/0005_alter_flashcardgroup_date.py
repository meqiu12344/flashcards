# Generated by Django 4.2.7 on 2023-12-21 20:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcardApp', '0004_alter_flashcardgroup_cardquantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcardgroup',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 21, 21, 32, 8, 572496)),
        ),
    ]
