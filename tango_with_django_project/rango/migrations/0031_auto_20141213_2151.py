# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0030_auto_20141213_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 21, 51, 31, 677510)),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 21, 51, 31, 677471)),
        ),
    ]
