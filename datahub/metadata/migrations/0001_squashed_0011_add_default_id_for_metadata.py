# Generated by Django 2.0.2 on 2018-02-09 14:49
from pathlib import PurePath

from django.db import migrations, models
import django.db.models.deletion
import uuid
from datahub.core.migration_utils import load_yaml_data_in_migration


def load_initial_countries(apps, schema_editor):
    load_yaml_data_in_migration(
        apps,
        PurePath(__file__).parent / '0001_initial_countries.yaml',
    )


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'countries',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EmployeeRange',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UKRegion',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TeamRole',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='Permission groups associated with this team.', related_name='team_roles', related_query_name='team_roles', to='auth.Group', verbose_name='team role permission groups')),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='metadata.Country')),
                ('uk_region', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='metadata.UKRegion')),
                ('role', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='teams', to='metadata.TeamRole')),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TurnoverRange',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='HeadquarterType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CompanyClassification',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='FDIType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvestmentBusinessActivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'investment business activities',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvestmentProjectStage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvestmentStrategicDriver',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InvestmentType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReferralSourceActivity',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'referral source activities',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReferralSourceMarketing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ReferralSourceWebsite',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='SalaryRange',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FDIValue',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.RunPython(load_initial_countries, migrations.RunPython.noop),
    ]
