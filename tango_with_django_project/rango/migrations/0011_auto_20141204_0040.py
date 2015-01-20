# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0010_userprofile_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='bgpicture',
            field=models.ImageField(default=b'/Users/Tanner_Stults/Desktop/Django/git/tango_with_django_project/media/profile_bgimages/default.jpg', upload_to=b'profile_bgimages', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(default=b'First Name', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(default=b'Last Name', max_length=100),
            preserve_default=True,
        ),
    ]
