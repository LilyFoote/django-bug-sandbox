# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('through', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OneToTwo',
            new_name='One2Two',
        ),
        migrations.AlterField(
            model_name='one',
            name='twos',
            field=models.ManyToManyField(through='through.One2Two', to='through.Two'),
        ),
    ]
