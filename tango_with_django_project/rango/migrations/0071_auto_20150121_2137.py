# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0070_auto_20150121_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='endDate',
            field=models.DateField(default=datetime.date.today, blank=True),
        ),
    ]
