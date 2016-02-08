# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def move_name_to_base(apps, schema_editor):
    Child = apps.get_model('inherited', 'Child')

    Child.objects.update(name=models.F('old_name'))


def move_name_to_child(apps, schema_editor):
    Child = apps.get_model('inherited', 'Child')

    Child.objects.update(old_name=models.F('name'))


class Migration(migrations.Migration):

    dependencies = [
        ('inherited', '0003_base_name'),
    ]

    operations = [
        migrations.RunPython(move_name_to_base, move_name_to_child),
    ]
