from contextlib import suppress
from operator import itemgetter

import factory
import pytest
from django.core.exceptions import FieldDoesNotExist
from rest_framework import status
from rest_framework.reverse import reverse

from datahub.core.test_utils import format_date_or_datetime
from .factories import ServiceFactory
from .. import urls
from ..models import Sector, Service
from ..registry import registry

# mark the whole module for db use
pytestmark = pytest.mark.django_db


def pytest_generate_tests(metafunc):
    """
    Parametrizes the tests that use the `metadata_view_name` fixture
    by getting all the metadata from the different apps.

    Parametrizes the tests that use the `ordered_mapping` fixture
    by getting all the ordered metadata from the different apps.
    """
    if 'metadata_view_name' in metafunc.fixturenames:
        view_names = registry.mappings.keys()
        metafunc.parametrize(
            'metadata_view_name',
            view_names,
            ids=[f'{view_name} metadata view' for view_name in view_names]
        )

    if 'ordered_mapping' in metafunc.fixturenames:
        view_data = []
        for view_id, mapping in registry.mappings.items():
            with suppress(FieldDoesNotExist):
                mapping.model._meta.get_field('order')  # check if model has field order
                view_data.append((view_id, mapping.model))

        metafunc.parametrize(
            'ordered_mapping',
            view_data,
            ids=[f'{view_data_item[0]} ordered metadata view' for view_data_item in view_data]
        )


def test_metadata_view_get(metadata_view_name, api_client):
    """Test a metadata view for 200 only."""
    url = reverse(viewname=metadata_view_name)
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK


def test_metadata_view_post(metadata_view_name, api_client):
    """Test views are read only."""
    url = reverse(viewname=metadata_view_name)
    response = api_client.post(url)
    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_metadata_view_put(metadata_view_name, api_client):
    """Test views are read only."""
    url = reverse(viewname=metadata_view_name)
    response = api_client.put(url)

    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_metadata_view_patch(metadata_view_name, api_client):
    """Test views are read only."""
    url = reverse(viewname=metadata_view_name)
    response = api_client.patch(url)

    assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED


def test_view_name_generation():
    """Test urls are generated correctly."""
    patterns = urls.urlpatterns
    assert {pattern.name for pattern in patterns} == frozenset(registry.mappings.keys())


def test_ordered_metadata_order_view(ordered_mapping, api_client):
    """
    Test that views with BaseOrderedConstantModel are ordered by the `order` field.
    """
    metadata_view_name, model = ordered_mapping

    url = reverse(viewname=metadata_view_name)
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    response_names = [value['name'] for value in response.json()]
    assert response_names == list(model.objects.order_by('order').values_list('name', flat=True))


def test_team_view(api_client):
    """Test that the team view returns role, uk_region and country as well."""
    url = reverse(viewname='team')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    teams = response.json()
    assert teams[0] == {
        'id': 'cff02898-9698-e211-a939-e4115bead28a',
        'name': 'Aberdeen City Council',
        'role': {
            'name': 'ATO',
            'id': '846cb21e-6095-e211-a939-e4115bead28a'
        },
        'uk_region': None,
        'country': {
            'name': 'United Kingdom',
            'id': '80756b9a-5d95-e211-a939-e4115bead28a'
        },
        'disabled_on': None,
    }

    disabled_team = next(
        team for team in teams
        if team['name'] == 'Business Information Centre Bhopal India'
    )
    assert disabled_team == {
        'id': 'ff8333c8-9698-e211-a939-e4115bead28a',
        'name': 'Business Information Centre Bhopal India',
        'role': {
            'name': 'Post',
            'id': '62329c18-6095-e211-a939-e4115bead28a'
        },
        'uk_region': None,
        'country': {
            'name': 'India',
            'id': '6f6a9ab2-5d95-e211-a939-e4115bead28a'
        },
        'disabled_on': '2013-03-31T16:21:07Z',
    }


class TestServiceView:
    """Tests for the /metadata/service/ view."""

    def test_list(self, api_client):
        """
        Test listing services.

        Services should include a list of contexts.
        """
        url = reverse(viewname='service')
        response = api_client.get(url)
        service = Service.objects.order_by('name')[0]

        assert response.status_code == status.HTTP_200_OK
        services = response.json()
        disabled_on = format_date_or_datetime(service.disabled_on) if service.disabled_on else None
        services[0]['contexts'] = sorted(services[0]['contexts'])

        assert services[0] == {
            'id': str(service.pk),
            'name': service.name,
            'contexts': sorted(service.contexts),
            'disabled_on': disabled_on,
        }
        assert len(services) == Service.objects.count()

    @pytest.mark.parametrize(
        'contexts',
        (
            [Service.CONTEXTS.interaction],
            ['non-existent-context'],
            [Service.CONTEXTS.interaction, Service.CONTEXTS.service_delivery],
        ),
    )
    def test_list_filter_by_has_any(self, api_client, contexts):
        """Test listing services, filtered by context."""
        test_data_contexts = (
            [Service.CONTEXTS.interaction],
            [Service.CONTEXTS.service_delivery],
            [Service.CONTEXTS.interaction, Service.CONTEXTS.service_delivery],
        )

        ServiceFactory.create_batch(
            len(test_data_contexts),
            contexts=factory.Iterator(test_data_contexts)
        )

        url = reverse(viewname='service')
        contexts_query_arg = ','.join(contexts)
        response = api_client.get(url, data={'contexts__has_any': contexts_query_arg})
        service_count_for_context = Service.objects.filter(contexts__overlap=contexts).count()

        assert response.status_code == status.HTTP_200_OK
        services = response.json()
        assert len(services) == service_count_for_context
        assert all(set(service['contexts']) & set(contexts) for service in services)


class TestSectorView:
    """Tests for the /metadata/sector/ view."""

    def test_list(self, api_client):
        """
        Test listing sectors.

        Sectors should be sorted by full name (path).
        """
        url = reverse(viewname='sector')
        response = api_client.get(url)
        sector = Sector.objects.order_by('lft')[0]

        assert response.status_code == status.HTTP_200_OK
        sectors = response.json()
        disabled_on = format_date_or_datetime(sector.disabled_on) if sector.disabled_on else None
        assert sectors[0] == {
            'id': str(sector.pk),
            'name': sector.name,
            'segment': sector.segment,
            'level': sector.level,
            'parent': {
                'id': str(sector.parent.pk),
                'name': sector.parent.name,
            } if sector.parent else None,
            'disabled_on': disabled_on,
        }

        assert sectors == list(sorted(sectors, key=itemgetter('name')))

    @pytest.mark.parametrize('level', (0, 1))
    def test_list_filter_by_level(self, api_client, level):
        """Test listing sectors, filter by level."""
        url = reverse(viewname='sector')
        response = api_client.get(url, data={'level__lte': level})
        sector_count_for_level = Sector.objects.filter(level__lte=level).count()

        assert response.status_code == status.HTTP_200_OK
        sectors = response.json()
        assert len(sectors) == sector_count_for_level
        assert all(sector['level'] <= level for sector in sectors)

    @pytest.mark.parametrize('method', ('POST', 'PATCH', 'PUT'))
    def test_unsupported_methods(self, api_client, method):
        """Test that POST, PATCH and PUT return a 405."""
        url = reverse(viewname='sector')
        response = api_client.generic(method, url)

        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED
