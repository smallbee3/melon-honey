# Generated by Django 2.0.2 on 2018-02-07 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('song', '0002_auto_20180208_0536'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='arranging',
            field=models.CharField(blank=True, max_length=30, verbose_name='편곡'),
        ),
        migrations.AddField(
            model_name='song',
            name='composing',
            field=models.CharField(blank=True, max_length=30, verbose_name='작곡'),
        ),
        migrations.AddField(
            model_name='song',
            name='flac',
            field=models.CharField(blank=True, max_length=100, verbose_name='FLAC'),
        ),
        migrations.AddField(
            model_name='song',
            name='genre',
            field=models.CharField(blank=True, max_length=100, verbose_name='장르'),
        ),
        migrations.AddField(
            model_name='song',
            name='lyrics',
            field=models.TextField(blank=True, max_length=10000, verbose_name='가사'),
        ),
        migrations.AddField(
            model_name='song',
            name='release_date',
            field=models.DateField(blank=True, null=True, verbose_name='발매일'),
        ),
        migrations.AddField(
            model_name='song',
            name='writing',
            field=models.CharField(blank=True, max_length=30, verbose_name='작사'),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=255, verbose_name='제목'),
        ),
    ]
