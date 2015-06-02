# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0092_auto_20150122_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(blank=True, max_length=200, choices=[(b'1', b'A.S.'), (b'2', b'A.A.'), (b'3', b'A.A.S.'), (b'4', b'B.A.'), (b'3', b'B.S.'), (b'4', b'B.F.A.'), (b'5', b'B.B.A.'), (b'6', b'B.Arch.'), (b'7', b'M.F.A.'), (b'8', b'M.A.'), (b'9', b'M.S. '), (b'10', b'M.A.'), (b'11', b'M.Res.'), (b'12', b'M.B.A.'), (b'13', b'LL.M.')]),
        ),
    ]
