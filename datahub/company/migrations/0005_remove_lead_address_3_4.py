# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-09 11:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_rename_advsor_fkeys_to_adviser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companieshousecompany',
            name='registered_address_3',
        ),
        migrations.RemoveField(
            model_name='companieshousecompany',
            name='registered_address_4',
        ),
        migrations.RemoveField(
            model_name='company',
            name='lead',
        ),
        migrations.RemoveField(
            model_name='company',
            name='registered_address_3',
        ),
        migrations.RemoveField(
            model_name='company',
            name='registered_address_4',
        ),
        migrations.RemoveField(
            model_name='company',
            name='trading_address_3',
        ),
        migrations.RemoveField(
            model_name='company',
            name='trading_address_4',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='address_3',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='address_4',
        ),
    ]
