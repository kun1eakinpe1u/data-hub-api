# Generated by Django 2.1.4 on 2018-12-11 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0033_add_new_policy_feedback_fields'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interaction',
            name='policy_feedback_notes',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='interaction',
            name='was_policy_feedback_provided',
            field=models.BooleanField(default=False, null=True),
        ),
    ]