# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-22 10:28
from __future__ import unicode_literals

from django.contrib.postgres.fields import CICharField
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0016_auto_20170216_1153'),
    ]

    operations = [
        migrations.RunSQL(
            sql='CREATE EXTENSION IF NOT EXISTS citext;',
            reverse_sql=migrations.RunSQL.noop,
        ),
        migrations.AlterField(
            model_name='advisor',
            name='email',
            field=CICharField(max_length=255, unique=True),
        ),
    ]
