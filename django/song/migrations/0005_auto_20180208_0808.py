# Generated by Django 2.0.2 on 2018-02-07 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0004_auto_20180208_0735'),
    ]

    operations = [
        migrations.RenameField(
            model_name='artistsong',
            old_name='Song',
            new_name='song',
        ),
        migrations.AlterField(
            model_name='song',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='album.Album', verbose_name='앨범'),
        ),
    ]
