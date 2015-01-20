# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0014_workexperience_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='dt',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 11, 2, 57, 58, 922496), blank=True),
            preserve_default=True,
        ),
    ]
