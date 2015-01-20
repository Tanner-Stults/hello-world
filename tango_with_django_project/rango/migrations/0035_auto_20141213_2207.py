# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0034_auto_20141213_2202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='user',
        ),
        migrations.DeleteModel(
            name='WorkExperience',
        ),
    ]
