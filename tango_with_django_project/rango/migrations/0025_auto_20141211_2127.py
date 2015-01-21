# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0024_auto_20141211_2125'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='endDate',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='startDate',
            field=models.DateTimeField(),
        ),
    ]
