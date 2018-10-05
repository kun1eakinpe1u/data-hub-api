from datahub.investment.evidence.models import EvidenceTag
from datahub.metadata.registry import registry


registry.register(
    metadata_id='evidence-tag',
    model=EvidenceTag,
)
