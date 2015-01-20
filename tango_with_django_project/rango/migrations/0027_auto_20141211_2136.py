# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0026_auto_20141211_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='endDate',
            field=models.DateField(default=b'2014-11-11'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='startDate',
            field=models.DateField(default=b'2014-11-11'),
        ),
    ]
