# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0068_auto_20150120_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='linkedIn',
            field=models.URLField(default='', blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='painting',
            name='art',
            field=models.ImageField(default=b'/Users/Tanner_Stults/Desktop/Django/git/tango_with_django_project/media/profile_bgimages/default.jpg', upload_to=b'paintings'),
        ),
    ]
