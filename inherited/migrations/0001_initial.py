# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Base',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Child',
            fields=[
                ('base_ptr', models.OneToOneField(parent_link=True, to='inherited.Base', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
            bases=('inherited.base',),
        ),
    ]
