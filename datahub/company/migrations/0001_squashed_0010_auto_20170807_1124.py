# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 10:29
from __future__ import unicode_literals

import datahub.company.models.adviser
import datahub.company.validators
from django.conf import settings
import django.contrib.postgres.fields.citext
import django.contrib.postgres.operations
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metadata', '0001_squashed_0012_auto_20170523_0940'),
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        django.contrib.postgres.operations.CITextExtension(
        ),
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(blank=True, max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255)),
                ('email', django.contrib.postgres.fields.citext.CICharField(max_length=255, unique=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Deselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('use_cdms_auth', models.BooleanField(default=False, help_text='Whether CDMS authentication has been enabled for this user')),
                ('dit_team', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.Team')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', datahub.company.models.adviser.AdviserManager()),
            ],
        ),
        migrations.CreateModel(
            name='CompaniesHouseCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('registered_address_1', models.CharField(max_length=255)),
                ('registered_address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('registered_address_town', models.CharField(max_length=255)),
                ('registered_address_county', models.CharField(blank=True, max_length=255, null=True)),
                ('registered_address_postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('company_number', models.CharField(max_length=255, unique=True)),
                ('company_category', models.CharField(blank=True, max_length=255)),
                ('company_status', models.CharField(blank=True, max_length=255)),
                ('sic_code_1', models.CharField(blank=True, max_length=255)),
                ('sic_code_2', models.CharField(blank=True, max_length=255)),
                ('sic_code_3', models.CharField(blank=True, max_length=255)),
                ('sic_code_4', models.CharField(blank=True, max_length=255)),
                ('uri', models.CharField(blank=True, max_length=255)),
                ('incorporation_date', models.DateField(null=True)),
                ('registered_address_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companieshousecompanys', to='metadata.Country')),
            ],
            options={
                'verbose_name_plural': 'Companies House companies',
            },
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('archived_on', models.DateTimeField(blank=True, null=True)),
                ('archived_reason', models.TextField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('registered_address_1', models.CharField(max_length=255)),
                ('registered_address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('registered_address_town', models.CharField(max_length=255)),
                ('registered_address_county', models.CharField(blank=True, max_length=255, null=True)),
                ('registered_address_postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('company_number', models.CharField(blank=True, max_length=255, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('alias', models.CharField(blank=True, help_text='Trading name', max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('website', models.CharField(blank=True, max_length=255, null=True, validators=[datahub.company.validators.RelaxedURLValidator])),
                ('trading_address_1', models.CharField(blank=True, max_length=255, null=True)),
                ('trading_address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('trading_address_town', models.CharField(blank=True, max_length=255, null=True)),
                ('trading_address_county', models.CharField(blank=True, max_length=255, null=True)),
                ('trading_address_postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('account_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companies', to=settings.AUTH_USER_MODEL)),
                ('archived_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('business_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.BusinessType')),
                ('classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.CompanyClassification')),
                ('employee_range', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.EmployeeRange')),
                ('export_to_countries', models.ManyToManyField(blank=True, related_name='company_export_to_countries', to='metadata.Country')),
                ('future_interest_countries', models.ManyToManyField(blank=True, related_name='company_future_interest_countries', to='metadata.Country')),
                ('headquarter_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.HeadquarterType')),
                ('one_list_account_owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='one_list_owned_companies', to=settings.AUTH_USER_MODEL)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='children', to='company.Company')),
                ('registered_address_country', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='companys', to='metadata.Country')),
                ('sector', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.Sector')),
                ('trading_address_country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='company_trading_address_country', to='metadata.Country')),
                ('turnover_range', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.TurnoverRange')),
                ('uk_region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.UKRegion')),
            ],
            options={
                'verbose_name_plural': 'companies',
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('archived', models.BooleanField(default=False)),
                ('archived_on', models.DateTimeField(blank=True, null=True)),
                ('archived_reason', models.TextField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('job_title', models.CharField(blank=True, max_length=255, null=True)),
                ('primary', models.BooleanField()),
                ('telephone_countrycode', models.CharField(max_length=255)),
                ('telephone_number', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('address_same_as_company', models.BooleanField(default=False)),
                ('address_1', models.CharField(blank=True, max_length=255, null=True)),
                ('address_2', models.CharField(blank=True, max_length=255, null=True)),
                ('address_town', models.CharField(blank=True, max_length=255, null=True)),
                ('address_county', models.CharField(blank=True, max_length=255, null=True)),
                ('address_postcode', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone_alternative', models.CharField(blank=True, max_length=255, null=True)),
                ('email_alternative', models.EmailField(blank=True, max_length=254, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('contactable_by_dit', models.BooleanField(default=False)),
                ('contactable_by_dit_partners', models.BooleanField(default=False)),
                ('contactable_by_email', models.BooleanField(default=True)),
                ('contactable_by_phone', models.BooleanField(default=True)),
                ('address_country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.Country')),
                ('adviser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contacts', to=settings.AUTH_USER_MODEL)),
                ('archived_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='company.Company')),
                ('title', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='metadata.Title')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='advisor',
            options={'verbose_name': 'adviser'},
        ),
        migrations.AddIndex(
            model_name='advisor',
            index=models.Index(fields=['first_name', 'last_name'], name='company_adv_first_n_61a74f_idx'),
        ),
        migrations.AddField(
            model_name='company',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='company',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='company',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, db_index=True, null=True),
        ),
    ]
