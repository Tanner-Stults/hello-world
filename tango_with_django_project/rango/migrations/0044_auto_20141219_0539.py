# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0043_painting'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='art',
            field=models.ImageField(default=b'/Users/Tanner_Stults/Desktop/Django/git/tango_with_django_project/media/profile_bgimages/default.jpg', upload_to=b'paintings'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='painting',
            name='medium',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
