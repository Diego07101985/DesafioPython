# Generated by Django 2.0.4 on 2018-04-30 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0006_auto_20180429_1811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, unique=True),
        ),
    ]
