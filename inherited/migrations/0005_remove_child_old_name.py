# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inherited', '0004_auto_20160208_1102'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='child',
            name='old_name',
        ),
    ]
