# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0018_auto_20141211_0316'),
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
