import pytest
from freezegun import freeze_time
from rest_framework import status
from rest_framework.reverse import reverse

from datahub.core import constants
from datahub.core.test_utils import LeelooTestCase
from .factories import CompanyFactory, ContactFactory

# mark the whole module for db use
pytestmark = pytest.mark.django_db


class AddContactTestCase(LeelooTestCase):
    """Add contact test case."""

    @freeze_time('2017-04-18 13:25:30.986208+00:00')
    def test_with_manual_address(self):
        """Test add with manual address."""
        company = CompanyFactory()

        url = reverse('api-v3:contact:list')
        response = self.api_client.post(url, {
            'title': {
                'id': constants.Title.admiral_of_the_fleet.value.id
            },
            'first_name': 'Oratio',
            'last_name': 'Nelson',
            'job_title': constants.Role.owner.value.name,
            'company': {
                'id': company.pk
            },
            'email': 'foo@bar.com',
            'email_alternative': 'foo2@bar.com',
            'primary': True,
            'telephone_countrycode': '+44',
            'telephone_number': '123456789',
            'telephone_alternative': '987654321',
            'address_same_as_company': False,
            'address_1': 'Foo st.',
            'address_2': 'adr 2',
            'address_town': 'London',
            'address_county': 'London',
            'address_country': {
                'id': constants.Country.united_kingdom.value.id
            },
            'address_postcode': 'SW1A1AA',
            'notes': 'lorem ipsum',
            'contactable_by_dit': False,
            'contactable_by_dit_partners': False,
            'contactable_by_email': True,
            'contactable_by_phone': True
        }, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == {
            'id': response.json()['id'],
            'title': {
                'id': constants.Title.admiral_of_the_fleet.value.id,
                'name': constants.Title.admiral_of_the_fleet.value.name
            },
            'first_name': 'Oratio',
            'last_name': 'Nelson',
            'job_title': constants.Role.owner.value.name,
            'company': {
                'id': company.pk,
                'name': company.name
            },
            'adviser': {
                'id': str(self.user.pk),
                'first_name': self.user.first_name,
                'last_name': self.user.last_name
            },
            'email': 'foo@bar.com',
            'email_alternative': 'foo2@bar.com',
            'primary': True,
            'telephone_countrycode': '+44',
            'telephone_number': '123456789',
            'telephone_alternative': '987654321',
            'address_same_as_company': False,
            'address_1': 'Foo st.',
            'address_2': 'adr 2',
            'address_town': 'London',
            'address_county': 'London',
            'address_country': {
                'id': constants.Country.united_kingdom.value.id,
                'name': constants.Country.united_kingdom.value.name
            },
            'address_postcode': 'SW1A1AA',
            'notes': 'lorem ipsum',
            'contactable_by_dit': False,
            'contactable_by_dit_partners': False,
            'contactable_by_email': True,
            'contactable_by_phone': True,
            'archived': False,
            'archived_by': None,
            'archived_on': None,
            'archived_reason': None,
            'created_on': '2017-04-18T13:25:30.986208'
        }

    def test_with_address_same_as_company(self):
        """Test add new contact with same address as company."""
        url = reverse('api-v3:contact:list')
        response = self.api_client.post(url, {
            'first_name': 'Oratio',
            'last_name': 'Nelson',
            'company': {
                'id': CompanyFactory().pk
            },
            'email': 'foo@bar.com',
            'telephone_countrycode': '+44',
            'telephone_number': '123456789',
            'address_same_as_company': True,
            'primary': True
        }, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        response_data = response.json()

        assert response_data['address_same_as_company']
        assert not response_data['address_1']
        assert not response_data['address_2']
        assert not response_data['address_country']
        assert not response_data['address_county']
        assert not response_data['address_postcode']
        assert not response_data['address_town']

    def test_defaults(self):
        """Test defaults when adding an item."""
        url = reverse('api-v3:contact:list')
        response = self.api_client.post(url, {
            'first_name': 'Oratio',
            'last_name': 'Nelson',
            'company': {
                'id': CompanyFactory().pk
            },
            'email': 'foo@bar.com',
            'telephone_countrycode': '+44',
            'telephone_number': '123456789',
            'address_same_as_company': True,
            'primary': True
        }, format='json')

        assert response.status_code == status.HTTP_201_CREATED
        response_data = response.data
        assert not response_data['title']
        assert not response_data['telephone_alternative']
        assert response_data['address_same_as_company']
        assert not response_data['email_alternative']
        assert not response_data['address_1']
        assert not response_data['address_2']
        assert not response_data['address_town']
        assert not response_data['address_county']
        assert not response_data['address_country']
        assert not response_data['address_postcode']
        assert not response_data['notes']
        assert not response_data['contactable_by_dit']
        assert not response_data['contactable_by_dit_partners']
        assert response_data['contactable_by_email']
        assert response_data['contactable_by_phone']

    def test_fails_with_invalid_email_address(self):
        """Test that fails if the email address is invalid."""
        url = reverse('api-v3:contact:list')
        response = self.api_client.post(url, {
            'first_name': 'Oratio',
            'last_name': 'Nelson',
            'company': {
                'id': CompanyFactory().pk
            },
            'email': 'invalid dot com',
            'telephone_countrycode': '+44',
            'telephone_number': '123456789',
            'address_same_as_company': True,
            'primary': True
        }, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {
            'email': ['Enter a valid email address.']
        }

    def test_fails_without_address(self):
        """Test that fails without any address."""
        url = reverse('api-v3:contact:list')
        response = self.api_client.post(url, {
            'first_name': 'Oratio',
            'last_name': 'Nelson',
            'company': {
                'id': CompanyFactory().pk
            },
            'email': 'foo@bar.com',
            'telephone_countrycode': '+44',
            'telephone_number': '123456789',
            'primary': True
        }, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {
            'address_same_as_company': ['Please select either address_same_as_company or enter an address manually.']
        }

    def test_fails_with_only_partial_manual_address(self):
        """Test that fails if only partial manual address supplied."""
        url = reverse('api-v3:contact:list')
        response = self.api_client.post(url, {
            'first_name': 'Oratio',
            'last_name': 'Nelson',
            'company': {
                'id': CompanyFactory().pk
            },
            'email': 'foo@bar.com',
            'telephone_countrycode': '+44',
            'telephone_number': '123456789',
            'address_1': 'test',
            'primary': True
        }, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {
            'address_country': ['This field may not be null.'],
            'address_town': ['This field may not be null.']
        }

    def test_fails_with_contact_preferences_not_set(self):
        """Test that fails without any contact preference."""
        url = reverse('api-v3:contact:list')
        response = self.api_client.post(url, {
            'first_name': 'Oratio',
            'last_name': 'Nelson',
            'company': {
                'id': CompanyFactory().pk
            },
            'email': 'foo@bar.com',
            'telephone_countrycode': '+44',
            'telephone_number': '123456789',
            'address_same_as_company': True,
            'contactable_by_email': False,
            'contactable_by_phone': False,
            'primary': True
        }, format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        assert response.data == {
            'contactable_by_email': [
                'A contact should have at least one way of being contacted. '
                'Please select either email or phone, or both'
            ],
            'contactable_by_phone': [
                'A contact should have at least one way of being contacted. '
                'Please select either email or phone, or both'
            ]
        }


class EditContactTestCase(LeelooTestCase):
    """Edit contact test case."""

    @freeze_time('2017-04-18 13:25:30.986208+00:00')
    def test_patch(self):
        """Test that it successfully patch an existing contact."""
        company = CompanyFactory()

        contact = ContactFactory(
            title_id=constants.Title.admiral_of_the_fleet.value.id,
            first_name='Oratio',
            last_name='Nelson',
            job_title=constants.Role.owner.value.name,
            company=company,
            email='foo@bar.com',
            email_alternative='foo2@bar.com',
            primary=True,
            adviser=self.user,
            telephone_countrycode='+44',
            telephone_number='123456789',
            telephone_alternative='987654321',
            address_same_as_company=False,
            address_1='Foo st.',
            address_2='adr 2',
            address_town='London',
            address_county='London',
            address_country_id=constants.Country.united_kingdom.value.id,
            address_postcode='SW1A1AA',
            notes='lorem ipsum',
            contactable_by_dit=False,
            contactable_by_dit_partners=False,
            contactable_by_email=True,
            contactable_by_phone=True
        )

        url = reverse('api-v3:contact:detail', kwargs={'pk': contact.pk})
        response = self.api_client.patch(url, {
            'first_name': 'New Oratio',
        }, format='json')

        assert response.status_code == status.HTTP_200_OK, response.data
        assert response.json() == {
            'id': response.json()['id'],
            'title': {
                'id': constants.Title.admiral_of_the_fleet.value.id,
                'name': constants.Title.admiral_of_the_fleet.value.name
            },
            'first_name': 'New Oratio',
            'last_name': 'Nelson',
            'job_title': constants.Role.owner.value.name,
            'company': {
                'id': company.pk,
                'name': company.name
            },
            'email': 'foo@bar.com',
            'email_alternative': 'foo2@bar.com',
            'primary': True,
            'adviser': {
                'id': str(self.user.pk),
                'first_name': self.user.first_name,
                'last_name': self.user.last_name
            },
            'telephone_countrycode': '+44',
            'telephone_number': '123456789',
            'telephone_alternative': '987654321',
            'address_same_as_company': False,
            'address_1': 'Foo st.',
            'address_2': 'adr 2',
            'address_town': 'London',
            'address_county': 'London',
            'address_country': {
                'id': constants.Country.united_kingdom.value.id,
                'name': constants.Country.united_kingdom.value.name
            },
            'address_postcode': 'SW1A1AA',
            'notes': 'lorem ipsum',
            'contactable_by_dit': False,
            'contactable_by_dit_partners': False,
            'contactable_by_email': True,
            'contactable_by_phone': True,
            'archived': False,
            'archived_by': None,
            'archived_on': None,
            'archived_reason': None,
            'created_on': '2017-04-18T13:25:30.986208'
        }


class ArchiveContactTestCase(LeelooTestCase):
    """Archive/unarchive contact test case."""

    def test_archive_without_reason(self):
        """Test archive contact without providing a reason."""
        contact = ContactFactory()
        url = reverse('api-v3:contact:archive', kwargs={'pk': contact.pk})
        response = self.api_client.post(url)

        assert response.data['archived']
        assert response.data['archived_by'] == {
            'id': str(self.user.pk),
            'first_name': self.user.first_name,
            'last_name': self.user.last_name
        }
        assert response.data['archived_reason'] == ''
        assert response.data['id'] == contact.pk

    def test_archive_with_reason(self):
        """Test archive contact providing a reason."""
        contact = ContactFactory()
        url = reverse('api-v3:contact:archive', kwargs={'pk': contact.pk})
        response = self.api_client.post(url, {'reason': 'foo'})

        assert response.data['archived']
        assert response.data['archived_by'] == {
            'id': str(self.user.pk),
            'first_name': self.user.first_name,
            'last_name': self.user.last_name
        }
        assert response.data['archived_reason'] == 'foo'
        assert response.data['id'] == contact.pk

    def test_unarchive_get(self):
        """Test unarchiving a contact using GET."""
        contact = ContactFactory(archived=True, archived_reason='foo')
        url = reverse('api-v3:contact:unarchive', kwargs={'pk': contact.pk})
        response = self.api_client.get(url)

        assert not response.data['archived']
        assert not response.data['archived_by']
        assert response.data['archived_reason'] == ''
        assert response.data['id'] == contact.pk

    def test_unarchive_post(self):
        """Test unarchiving a contact using POST."""
        contact = ContactFactory(archived=True, archived_reason='foo')
        url = reverse('api-v3:contact:unarchive', kwargs={'pk': contact.pk})
        response = self.api_client.post(url)

        assert not response.data['archived']
        assert not response.data['archived_by']
        assert response.data['archived_reason'] == ''
        assert response.data['id'] == contact.pk


class ViewContactTestCase(LeelooTestCase):
    """View contact test case."""

    @freeze_time('2017-04-18 13:25:30.986208+00:00')
    def test_view(self):
        """Test view."""
        company = CompanyFactory()

        contact = ContactFactory(
            title_id=constants.Title.admiral_of_the_fleet.value.id,
            first_name='Oratio',
            last_name='Nelson',
            job_title=constants.Role.owner.value.name,
            company=company,
            email='foo@bar.com',
            email_alternative='foo2@bar.com',
            primary=True,
            adviser=self.user,
            telephone_countrycode='+44',
            telephone_number='123456789',
            telephone_alternative='987654321',
            address_same_as_company=False,
            address_1='Foo st.',
            address_2='adr 2',
            address_town='London',
            address_county='London',
            address_country_id=constants.Country.united_kingdom.value.id,
            address_postcode='SW1A1AA',
            notes='lorem ipsum',
            contactable_by_dit=False,
            contactable_by_dit_partners=False,
            contactable_by_email=True,
            contactable_by_phone=True
        )
        url = reverse('api-v3:contact:detail', kwargs={'pk': contact.pk})
        response = self.api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.json() == {
            'id': response.json()['id'],
            'title': {
                'id': constants.Title.admiral_of_the_fleet.value.id,
                'name': constants.Title.admiral_of_the_fleet.value.name
            },
            'first_name': 'Oratio',
            'last_name': 'Nelson',
            'job_title': constants.Role.owner.value.name,
            'company': {
                'id': company.pk,
                'name': company.name
            },
            'adviser': {
                'id': str(self.user.pk),
                'first_name': self.user.first_name,
                'last_name': self.user.last_name
            },
            'email': 'foo@bar.com',
            'email_alternative': 'foo2@bar.com',
            'primary': True,
            'telephone_countrycode': '+44',
            'telephone_number': '123456789',
            'telephone_alternative': '987654321',
            'address_same_as_company': False,
            'address_1': 'Foo st.',
            'address_2': 'adr 2',
            'address_town': 'London',
            'address_county': 'London',
            'address_country': {
                'id': constants.Country.united_kingdom.value.id,
                'name': constants.Country.united_kingdom.value.name
            },
            'address_postcode': 'SW1A1AA',
            'notes': 'lorem ipsum',
            'contactable_by_dit': False,
            'contactable_by_dit_partners': False,
            'contactable_by_email': True,
            'contactable_by_phone': True,
            'archived': False,
            'archived_by': None,
            'archived_on': None,
            'archived_reason': None,
            'created_on': '2017-04-18T13:25:30.986208'
        }


class ContactListTestCase(LeelooTestCase):
    """List/filter contacts test case."""

    def test_all(self):
        """Test getting all contacts"""
        ContactFactory.create_batch(5)

        url = reverse('api-v3:contact:list')
        response = self.api_client.get(url)

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 5

    def test_filter_by_company(self):
        """Test getting contacts by company id"""
        company1 = CompanyFactory()
        company2 = CompanyFactory()

        ContactFactory.create_batch(3, company=company1)
        contacts = ContactFactory.create_batch(2, company=company2)

        url = reverse('api-v3:contact:list')
        response = self.api_client.get(url, {'company_id': company2.id})

        assert response.status_code == status.HTTP_200_OK
        assert response.data['count'] == 2
        assert {contact['id'] for contact in response.data['results']} == {contact.id for contact in contacts}
