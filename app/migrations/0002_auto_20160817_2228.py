# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-17 14:28
from __future__ import unicode_literals

import app.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='add_time',
            field=app.models.TIMESTAMP(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_time',
            field=app.models.TIMESTAMP(null=True),
        ),
    ]
