# Generated by Django 2.0.2 on 2018-02-02 09:39

from pathlib import PurePath

from django.db import migrations, models
import uuid
from datahub.core.migration_utils import load_yaml_data_in_migration


def load_initial_statuses(apps, schema_editor):
    load_yaml_data_in_migration(
        apps,
        PurePath(__file__).parent / '0020_initial_statuses.yaml'
    )


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0001_squashed_0019_rename_default_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceDeliveryStatus',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
                ('order', models.FloatField(default=0.0)),
            ],
            options={
                'ordering': ('order',),
                'abstract': False,
            },
        ),
        migrations.RunPython(load_initial_statuses, migrations.RunPython.noop)
    ]
