# Generated by Django 3.2.1 on 2021-05-06 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='musicitem',
            name='last_performed',
        ),
        migrations.RemoveField(
            model_name='musicitem',
            name='rating',
        ),
    ]
