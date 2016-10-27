"""
These tests rely on the metadata.yaml fixture to be imported,
Check conftest.py in the root folder for the importing mechanism.
"""

import pytest
from django.conf import settings

from django.urls import reverse
from django.utils.timezone import now
from rest_framework import status

from core import constants
from es.services import document_exists
from es.utils import get_elasticsearch_client

from .factories import AdvisorFactory, CompanyFactory, ContactFactory, InteractionFactory

# mark the whole module for db use
pytestmark = pytest.mark.django_db


def test_interaction_detail_view(api_client):
    """Interaction detail view."""

    interaction = InteractionFactory()
    url = reverse('interaction-detail', kwargs={'pk': interaction.pk})
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == interaction.pk


def test_add_interaction(api_client):
    """Test add new interaction."""

    url = reverse('interaction-list')
    response = api_client.post(url, {
        'interaction_type': constants.InteractionType.business_card.value.id,
        'subject': 'whatever',
        'date_of_interaction': now().isoformat(),
        'dit_advisor': AdvisorFactory().pk,
        'notes': 'hello',
        'company': CompanyFactory().pk,
        'contact': ContactFactory().pk,
        'service': constants.Service.trade_enquiry.value.id,
        'dit_team': constants.Team.healthcare_uk.value.id
    })

    assert response.status_code == status.HTTP_201_CREATED

    # make sure we're writing to ES
    es_client = get_elasticsearch_client()
    assert document_exists(
        client=es_client,
        doc_type='company_interaction',
        document_id=response.data['id']
    )


def test_modify_interaction(api_client):
    """Modify an existing interaction."""

    contact = InteractionFactory(subject='I am a subject')

    url = reverse('interaction-detail', kwargs={'pk': contact.pk})
    response = api_client.patch(url, {
        'subject': 'I am another subject',
    })

    assert response.status_code == status.HTTP_200_OK
    assert response.data['subject'] == 'I am another subject'

    # make sure we're writing to ES
    es_client = get_elasticsearch_client()
    es_result = es_client.get(
        index=settings.ES_INDEX,
        doc_type='company_interaction',
        id=response.data['id'],
        realtime=True
    )
    assert es_result['_source']['subject'] == 'I am another subject'


def test_archive_interaction_no_reason(api_client):
    """Test archive interaction without providing a reason."""

    interaction = InteractionFactory()
    url = reverse('interaction-archive', kwargs={'pk': interaction.pk})
    response = api_client.post(url)

    assert response.data['archived']
    assert response.data['archived_reason'] == ''
    assert response.data['id'] == interaction.pk

    # make sure we're writing to ES
    es_client = get_elasticsearch_client()
    es_result = es_client.get(
        index=settings.ES_INDEX,
        doc_type='company_interaction',
        id=response.data['id'],
        realtime=True
    )
    assert es_result['_source']['archived']
    assert es_result['_source']['archived_reason'] == ''


def test_archive_interaction_reason(api_client):
    """Test archive interaction providing a reason."""

    interaction = InteractionFactory()
    url = reverse('interaction-archive', kwargs={'pk': interaction.pk})
    response = api_client.post(url, {'reason': 'foo'})

    assert response.data['archived']
    assert response.data['archived_reason'] == 'foo'
    assert response.data['id'] == interaction.pk

    # make sure we're writing to ES
    es_client = get_elasticsearch_client()
    es_result = es_client.get(
        index=settings.ES_INDEX,
        doc_type='company_interaction',
        id=response.data['id'],
        realtime=True
    )
    assert es_result['_source']['archived']
    assert es_result['_source']['archived_reason'] == 'foo'
