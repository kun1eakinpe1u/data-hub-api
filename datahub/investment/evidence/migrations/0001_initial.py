# Generated by Django 2.0.8 on 2018-08-14 12:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('documents', '0004_add_bucket_id_status_av_reason_constraint'),
        ('investment', '0047_remove_iprojectdocument'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvidenceDocument',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('modified_on', models.DateTimeField(auto_now=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('original_filename', models.CharField(max_length=255)),
                ('comment', models.TextField(blank=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('document', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='documents.Document')),
                ('investment_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='evidence_documents', to='investment.InvestmentProject')),
                ('modified_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'investment project evidence document',
            },
        ),
        migrations.CreateModel(
            name='EvidenceTag',
            fields=[
                ('disabled_on', models.DateTimeField(blank=True, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('name', models.TextField(blank=True)),
            ],
            options={
                'ordering': ('name',),
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='evidencedocument',
            name='tags',
            field=models.ManyToManyField(related_name='_evidencedocument_tags_+', to='evidence.EvidenceTag'),
        ),
    ]
