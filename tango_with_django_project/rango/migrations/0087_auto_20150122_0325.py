# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0086_auto_20150122_0324'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='current',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='info',
            field=models.CharField(max_length=1000, blank=True),
        ),
    ]
