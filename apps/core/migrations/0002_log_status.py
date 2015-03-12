# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='status',
            field=models.CharField(default=None, max_length=3, choices=[(b'1', b'Alterado'), (b'2', b'Deletado')]),
            preserve_default=False,
        ),
    ]
