# Generated by Django 3.2.1 on 2021-05-05 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MusicItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inventory_num', models.CharField(max_length=20)),
                ('title', models.CharField(max_length=255)),
                ('composer_last', models.CharField(max_length=255)),
                ('composer_first', models.CharField(max_length=255)),
                ('arranger_last', models.CharField(max_length=255)),
                ('arranger_first', models.CharField(max_length=255)),
                ('ensemble', models.CharField(max_length=20)),
                ('style', models.CharField(max_length=20)),
                ('difficulty', models.CharField(max_length=20)),
                ('rating', models.IntegerField()),
                ('last_performed', models.DateField()),
                ('organized', models.BooleanField()),
                ('notes', models.CharField(max_length=255)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
