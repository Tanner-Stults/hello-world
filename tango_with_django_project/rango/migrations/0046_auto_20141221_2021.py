# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0045_auto_20141220_0752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='info',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='website',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='currentJob',
            field=models.CharField(default='student', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='currentLocation',
            field=models.CharField(default='Ithaca, NY', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='education',
            field=models.CharField(default='Cornell University', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='industry',
            field=models.CharField(default='Private Equity', max_length=200),
            preserve_default=False,
        ),
    ]
