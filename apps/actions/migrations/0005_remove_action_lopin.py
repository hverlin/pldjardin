# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-01 21:07
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('actions', '0004_auto_20160501_2218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='action',
            name='lopin',
        ),
    ]
