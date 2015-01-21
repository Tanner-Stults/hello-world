# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0011_auto_20141204_0040'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='bgpicture',
            new_name='bgPicture',
        ),
    ]
