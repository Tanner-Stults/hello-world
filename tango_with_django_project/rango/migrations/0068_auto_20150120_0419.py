# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0067_auto_20150120_0319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bgPicture',
            field=models.ImageField(upload_to=b'profile_bgimages', blank=True),
        ),
    ]
