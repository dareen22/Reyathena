# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20160902_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='athlete',
            name='image',
        ),
        migrations.RemoveField(
            model_name='athlete',
            name='name',
        ),
    ]
