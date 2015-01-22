# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0080_auto_20150122_0314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='info',
            field=models.CharField(max_length=1000),
        ),
    ]
