# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-12 16:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opm_app', '0004_auto_20170412_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='brother_name',
            field=models.CharField(max_length=100),
        ),
    ]