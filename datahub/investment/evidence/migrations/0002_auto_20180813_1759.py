# Generated by Django 2.0.8 on 2018-08-13 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evidence', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='evidencegroup',
            options={'default_permissions': ('add_all', 'change_all', 'delete'), 'permissions': (('read_all_evidencegroup', 'Can read all proposition'), ('read_associated_evidencegroup', 'Can read evidence group for associated investment projects'), ('add_associated_evidencegroup', 'Can add evidence group for associated investment projects'), ('change_associated_evidencegroup', 'Can change evidence group for associated investment projects'))},
        ),
    ]