# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0061_auto_20150101_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='coords',
            field=models.CharField(default='', max_length=100, blank=True),
            preserve_default=False,
        ),
    ]
