# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0091_auto_20150122_0343'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='current',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='education',
            name='endDate',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
