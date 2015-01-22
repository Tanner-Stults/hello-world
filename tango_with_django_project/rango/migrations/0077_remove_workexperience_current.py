# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0076_auto_20150121_2150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='current',
        ),
    ]
