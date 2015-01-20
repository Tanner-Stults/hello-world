# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0038_auto_20141213_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='endDate',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='startDate',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
