# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0079_auto_20150121_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='info',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
