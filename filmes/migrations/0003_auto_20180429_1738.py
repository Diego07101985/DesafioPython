# Generated by Django 2.0.4 on 2018-04-29 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filmes', '0002_auto_20180429_0315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='actor',
            name='filme',
        ),
        migrations.AddField(
            model_name='actor',
            name='filmes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='actors', to='filmes.Filme'),
        ),
    ]
