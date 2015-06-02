# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0094_auto_20150122_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='info',
            field=models.TextField(max_length=1000, blank=True),
        ),
    ]
