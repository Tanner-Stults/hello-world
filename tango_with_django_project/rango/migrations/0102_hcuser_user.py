# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rango', '0101_hcuser'),
    ]

    operations = [
        migrations.AddField(
            model_name='hcuser',
            name='user',
            field=models.OneToOneField(default='', editable=False, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
