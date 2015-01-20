# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0048_userprofile_currentcompany'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(max_length=100),
        ),
    ]
