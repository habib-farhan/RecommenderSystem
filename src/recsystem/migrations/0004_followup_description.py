# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recsystem', '0003_followup'),
    ]

    operations = [
        migrations.AddField(
            model_name='followup',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]
