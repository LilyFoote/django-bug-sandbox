# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inherited', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='child',
            old_name='name',
            new_name='old_name',
        ),
    ]
