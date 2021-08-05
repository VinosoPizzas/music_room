# Generated by Django 3.2.5 on 2021-07-29 22:11

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_room_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default=api.models.generates_unique_code, max_length=6, unique=True),
        ),
    ]
