# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0064_auto_20150108_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='currentJob',
            new_name='currentPosition',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='previousJob',
            new_name='previousPosition',
        ),
    ]
