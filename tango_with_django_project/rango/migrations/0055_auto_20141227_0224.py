# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0054_auto_20141227_0056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name=b'cropping',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
        ),
    ]
