# Generated by Django 2.0.2 on 2018-02-08 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0011_song_artist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='song',
            name='artist',
        ),
    ]
