# Generated by Django 3.2.5 on 2021-07-29 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='code',
            field=models.CharField(default='', max_length=6, unique=True),
        ),
    ]
