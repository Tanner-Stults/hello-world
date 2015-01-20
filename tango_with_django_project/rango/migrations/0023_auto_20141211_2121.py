# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0022_auto_20141211_2119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='endDate',
            field=models.DateField(default=datetime.date(2014, 12, 11)),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='startDate',
            field=models.DateField(default=datetime.date(2014, 12, 11)),
        ),
    ]
