# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 19:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='price',
            field=models.FloatField(),
        ),
    ]
