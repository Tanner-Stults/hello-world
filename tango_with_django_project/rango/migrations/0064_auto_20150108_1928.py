# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0063_auto_20150102_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='previousCompany',
            field=models.CharField(default='American Capital', max_length=200, blank=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='previousJob',
            field=models.CharField(default='Partner', max_length=200, blank=True),
            preserve_default=False,
        ),
    ]
