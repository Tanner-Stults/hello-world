# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0040_auto_20141213_2228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='endDate',
            field=models.DateField(default=b'2014-12-12'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='startDate',
            field=models.DateField(default=b'2014-12-12'),
        ),
    ]
