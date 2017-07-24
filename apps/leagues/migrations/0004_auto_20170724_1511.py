# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-24 19:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leagues', '0003_auto_20161031_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='league',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leagues.League'),
        ),
    ]