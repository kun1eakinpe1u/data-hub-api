# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-08 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0014_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='po_number',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
