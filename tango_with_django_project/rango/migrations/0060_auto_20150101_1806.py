# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0059_auto_20141228_2213'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name=b'cropping',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='picture',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
        ),
    ]
