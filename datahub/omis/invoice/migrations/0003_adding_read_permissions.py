# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-24 12:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('omis-invoice', '0002_invoice_payment_due_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invoice',
            options={'permissions': (('read_invoice', 'Can read invoice'),)},
        ),
    ]