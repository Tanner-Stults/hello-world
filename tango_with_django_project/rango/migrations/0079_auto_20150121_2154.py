# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0078_workexperience_current'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='current',
            field=models.BooleanField(default=None),
        ),
    ]
