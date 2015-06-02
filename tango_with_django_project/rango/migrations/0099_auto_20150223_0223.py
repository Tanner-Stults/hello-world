# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0098_auto_20150223_0037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cookies',
            options={'ordering': ['domain'], 'verbose_name_plural': 'Cookies'},
        ),
    ]
