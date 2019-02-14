import uuid

from django.conf import settings
from django.db import models

from datahub.core import reversion
from datahub.core.models import (
    BaseModel,
    BaseOrderedConstantModel,
)


MAX_LENGTH = settings.CHAR_FIELD_MAX_LENGTH


@reversion.register_base_model()
class InvestorProfile(BaseModel):
    """Investor profile model"""

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
    )

    investor_company = models.ForeignKey(
        'company.Company',
        related_name='investor_profiles',
        on_delete=models.CASCADE,
    )

    profile_type = models.ForeignKey(
        'ProfileType',
        related_name='+',
        on_delete=models.PROTECT,
    )

    investor_type = models.ForeignKey(
        'InvestorType',
        related_name='+',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    investable_capital = models.DecimalField(
        max_digits=19,
        decimal_places=0,
        blank=True,
        null=True,
        help_text='Investable capital amount in USD',
    )

    investor_description = models.TextField(
        blank=True,
        null=True,
    )

    client_contacts = models.ManyToManyField(
        'company.Contact',
        related_name='investor_profiles',
        blank=True,
    )

    dit_relationship_manager = models.ForeignKey(
        'company.Advisor',
        related_name='investor_profiles',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    dit_advisors = models.ManyToManyField(
        'company.Advisor',
        related_name='+',
        blank=True,
    )

    relationship_health = models.ForeignKey(
        'RelationshipHealth',
        related_name='+',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    background_checks_conducted = models.ForeignKey(
        'BackgroundChecksConducted',
        related_name='+',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    deal_ticket_sizes = models.ManyToManyField(
        'DealTicketSize',
        related_name='+',
        blank=True,
    )

    asset_classes_of_interest = models.ManyToManyField(
        'AssetClassInterest',
        related_name='+',
        blank=True,
    )

    investment_types = models.ManyToManyField(
        'LargeCapitalInvestmentType',
        related_name='+',
        blank=True,
    )

    minimum_return_rate = models.ForeignKey(
        'ReturnRate',
        related_name='+',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    time_horizons = models.ManyToManyField(
        'TimeHorizon',
        related_name='+',
        blank=True,
    )

    restrictions = models.ManyToManyField(
        'Restriction',
        related_name='+',
        blank=True,
    )

    construction_risks = models.ManyToManyField(
        'ConstructionRisk',
        related_name='+',
        blank=True,
    )

    minimum_equity_percentage = models.ForeignKey(
        'EquityPercentage',
        related_name='+',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    desired_deal_roles = models.ManyToManyField(
        'DesiredDealRole',
        related_name='+',
        blank=True,
    )

    uk_region_locations = models.ManyToManyField(
        'metadata.UKRegion',
        related_name='+',
        blank=True,
        verbose_name='possible UK regions',
    )

    other_countries_considering = models.ManyToManyField(
        'metadata.Country',
        related_name='+',
        blank=True,
        help_text='The other countries being considered for investment',
    )

    notes_on_locations = models.TextField(
        blank=True,
        null=True,
    )

    class Meta:
        unique_together = ('investor_company', 'profile_type')


class ProfileType(BaseOrderedConstantModel):
    """Investor profile type metadata"""


class InvestorType(BaseOrderedConstantModel):
    """Investor type metadata"""


class RelationshipHealth(BaseOrderedConstantModel):
    """Relationship health metadata"""


class DealTicketSize(BaseOrderedConstantModel):
    """Deal ticket size metadata"""


class LargeCapitalInvestmentType(BaseOrderedConstantModel):
    """Large capital investment type metadata"""


class ReturnRate(BaseOrderedConstantModel):
    """Return rate metadata"""


class TimeHorizon(BaseOrderedConstantModel):
    """Investor time horizons metadata"""


class Restriction(BaseOrderedConstantModel):
    """Investor restrictions metadata"""


class ConstructionRisk(BaseOrderedConstantModel):
    """Investment construction risk metadata"""


class EquityPercentage(BaseOrderedConstantModel):
    """Equity percentage metadata"""


class DesiredDealRole(BaseOrderedConstantModel):
    """Desired deal role metadata"""


class BackgroundChecksConducted(BaseOrderedConstantModel):
    """Background checks conducted metadata"""


class AssetClassInterest(BaseOrderedConstantModel):
    """Asset class interest metadata"""

    asset_interest_sector = models.CharField(
        max_length=MAX_LENGTH,
        null=False,
        blank=False,
    )