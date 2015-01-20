# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0060_auto_20150101_1806'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name=b'cropping',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='currentCompany',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='currentJob',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='currentLocation',
            field=models.CharField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='education',
            field=models.CharField(max_length=400, blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='industry',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
