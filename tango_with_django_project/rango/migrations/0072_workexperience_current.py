# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0071_auto_20150121_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='current',
            field=models.NullBooleanField(),
            preserve_default=True,
        ),
    ]
