# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0047_auto_20141221_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='currentCompany',
            field=models.CharField(default='CoVenture', max_length=200),
            preserve_default=False,
        ),
    ]
