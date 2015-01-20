# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0066_auto_20150113_0306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='art',
            field=models.ImageField(default=b'/home/James2248/Hello-World/tango_with_django_project/media/profile_bgimages/default.jpg', upload_to=b'paintings'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bgPicture',
            field=models.ImageField(default=b'/home/James2248/Hello-World/tango_with_django_project/media/profile_bgimages/default.jpg', upload_to=b'profile_bgimages', blank=True),
        ),
    ]
