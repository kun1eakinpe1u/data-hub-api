# Generated by Django 2.1.4 on 2019-01-04 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0034_add_new_policy_feedback_field_defaults'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='kind',
            field=models.CharField(choices=[('interaction', 'Interaction'), ('service_delivery', 'Service delivery')], max_length=255),
        ),
    ]
