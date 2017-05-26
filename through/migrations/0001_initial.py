# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='One',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OneToTwo',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('one', models.ForeignKey(to='through.One')),
            ],
        ),
        migrations.CreateModel(
            name='Two',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='onetotwo',
            name='two',
            field=models.ForeignKey(to='through.Two'),
        ),
        migrations.AddField(
            model_name='one',
            name='twos',
            field=models.ManyToManyField(to='through.Two', through='through.OneToTwo'),
        ),
        migrations.AlterUniqueTogether(
            name='onetotwo',
            unique_together=set([('one', 'two')]),
        ),
    ]
