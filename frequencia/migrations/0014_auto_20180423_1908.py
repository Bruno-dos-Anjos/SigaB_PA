# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-23 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frequencia', '0013_auto_20180423_1907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frequencia',
            name='data',
            field=models.DateField(),
        ),
    ]
