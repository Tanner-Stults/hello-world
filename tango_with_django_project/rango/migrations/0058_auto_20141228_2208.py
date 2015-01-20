# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0057_auto_20141228_2203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name=b'cropping',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='picture',
        ),
    ]
