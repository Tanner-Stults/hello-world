# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0029_auto_20141213_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='endDate',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 21, 46, 2, 171175)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='startDate',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 13, 21, 46, 2, 171136)),
            preserve_default=True,
        ),
    ]
