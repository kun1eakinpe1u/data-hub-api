# Generated by Django 2.2.3 on 2019-07-24 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0009_multiaddressmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonListItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='support.Person')),
            ],
        ),
    ]
