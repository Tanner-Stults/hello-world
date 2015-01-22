# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0085_auto_20150122_0319'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='current',
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='info',
            field=models.CharField(max_length=1000),
        ),
    ]
