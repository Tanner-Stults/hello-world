# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0077_remove_workexperience_current'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='current',
            field=models.NullBooleanField(default=None),
            preserve_default=True,
        ),
    ]
