# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-27 07:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jardin', '0005_auto_20160426_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='jardin',
            name='composter',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='jardin',
            name='contact',
            field=models.EmailField(default='contact@lecontact.fr', help_text="Email de contact du jardin, ou le mail d'un responsable", max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jardin',
            name='site',
            field=models.CharField(blank=True, help_text='Le site web du jardin', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='jardin',
            name='nom',
            field=models.CharField(help_text='Nom du jardin', max_length=50),
        ),
        migrations.AlterField(
            model_name='jardin',
            name='restreint',
            field=models.BooleanField(default=False),
        ),
    ]
