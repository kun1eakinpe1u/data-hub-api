# Generated by Django 2.0.6 on 2018-06-05 14:22

from django.db import migrations, models


def copy_policy_areas(apps, schema_editor):
    """Copies policy_area to policy_areas."""
    interaction_model = apps.get_model('interaction', 'Interaction')

    interactions_with_policy_area = interaction_model.objects.filter(policy_area__isnull=False)
    for interaction in interactions_with_policy_area:
        interaction.policy_areas.add(interaction.policy_area)


class Migration(migrations.Migration):

    dependencies = [
        ('interaction', '0026_add_policy_feedback_permissions'),
    ]

    operations = [
        migrations.AddField(
            model_name='interaction',
            name='policy_areas',
            field=models.ManyToManyField(blank=True, related_name='interactions', to='interaction.PolicyArea'),
        ),
        migrations.RunPython(copy_policy_areas, migrations.RunPython.noop, elidable=True),
    ]
