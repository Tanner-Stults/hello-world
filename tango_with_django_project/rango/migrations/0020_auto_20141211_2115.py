# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0019_auto_20141211_2111'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='endDate',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='startDate',
            field=models.DateField(default=datetime.date.today),
            preserve_default=True,
        ),
    ]
