# Generated by Django 2.0.8 on 2018-08-03 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0029_remove-parent-from-django'),
        ('core', '0003_rename_read_permissions'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='advisor',
            options={'verbose_name': 'adviser'},
        ),
        migrations.AlterModelOptions(
            name='companieshousecompany',
            options={'verbose_name_plural': 'Companies House companies'},
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'permissions': (('view_company_document', 'Can view company document'), ('view_company_timeline', 'Can view company timeline')), 'verbose_name_plural': 'companies'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'permissions': (('view_contact_document', 'Can view contact document'),)},
        ),
    ]
