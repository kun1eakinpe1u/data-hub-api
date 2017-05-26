# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-23 09:40
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('metadata', '0011_correct_model_plural_names'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businesstype',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='companyclassification',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='country',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='employeerange',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='event',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='fditype',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='headquartertype',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='interactiontype',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='investmentbusinessactivity',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='investmentprojectphase',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='investmentstrategicdriver',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='investmenttype',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='nonfditype',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='referralsourceactivity',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='referralsourcemarketing',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='referralsourcewebsite',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='role',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='salaryrange',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='sector',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='service',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='servicedeliverystatus',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='team',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='title',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='turnoverrange',
            name='selectable',
        ),
        migrations.RemoveField(
            model_name='ukregion',
            name='selectable',
        ),
    ]
