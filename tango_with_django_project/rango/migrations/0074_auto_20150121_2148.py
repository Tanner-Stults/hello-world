# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0073_auto_20150121_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='current',
            field=models.BooleanField(default=None),
        ),
    ]
