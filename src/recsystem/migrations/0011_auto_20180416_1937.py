# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-16 17:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recsystem', '0010_remove_answer_answer_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='max_val',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='min_val',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
