# Generated by Django 2.0.2 on 2018-02-17 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artist', '0006_auto_20180208_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='img_profile',
            field=models.ImageField(upload_to='artist', verbose_name='프로필 이미지'),
        ),
    ]
