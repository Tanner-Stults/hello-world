# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0031_auto_20141213_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 21, 53, 13, 141477)),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 21, 53, 13, 141439)),
        ),
    ]
