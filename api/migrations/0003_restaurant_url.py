# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-22 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170922_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='url',
            field=models.TextField(default='--', verbose_name='画像'),
        ),
    ]
