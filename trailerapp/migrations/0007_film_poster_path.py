# Generated by Django 2.1.4 on 2018-12-17 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trailerapp', '0006_film_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='poster_path',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
