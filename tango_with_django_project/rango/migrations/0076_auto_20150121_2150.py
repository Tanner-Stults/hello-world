# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0075_auto_20150121_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='current',
            field=models.NullBooleanField(default=None),
        ),
    ]
