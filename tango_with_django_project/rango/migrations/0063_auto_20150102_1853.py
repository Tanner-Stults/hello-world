# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0062_userprofile_coords'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['user'], 'verbose_name_plural': 'Education'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['user']},
        ),
        migrations.AlterModelOptions(
            name='workexperience',
            options={'ordering': ['user']},
        ),
    ]
