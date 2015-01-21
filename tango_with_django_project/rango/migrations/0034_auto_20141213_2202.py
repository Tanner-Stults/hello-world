# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0033_auto_20141213_2201'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='endDate',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='startDate',
        ),
    ]
