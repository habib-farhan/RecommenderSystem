# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-09 15:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recsystem', '0009_auto_20180409_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='answer_label',
        ),
    ]
