# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-19 17:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recsystem', '0011_auto_20180416_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='followUp',
            field=models.BooleanField(default=False),
        ),
    ]