from django.conf import settings
from django.db import models
from django.utils.timezone import now


class BaseModel(models.Model):
    """Common fields for most of the models we use."""

    created_on = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    modified_on = models.DateTimeField(null=True, blank=True, auto_now=True)

    class Meta:  # noqa: D101
        abstract = True


class ArchivableModel(models.Model):
    """Handle model archivation."""

    archived = models.BooleanField(default=False)
    archived_on = models.DateTimeField(null=True)
    archived_reason = models.TextField(blank=True, null=True)
    archived_by = models.ForeignKey(settings.AUTH_USER_MODEL, null=True)

    class Meta:  # noqa: D101
        abstract = True

    def archive(self, user, reason=None):
        """Archive the model instance."""
        self.archived = True
        self.archived_by = user
        self.archived_reason = reason
        self.archived_on = now()
        self.save()

    def unarchive(self):
        """Unarchive the model instance."""
        self.archived = False
        self.archived_reason = ''
        self.archived_by = None
        self.archived_on = None
        self.save()


class BaseConstantModel(models.Model):
    """Constant tables for FKs."""

    id = models.UUIDField(primary_key=True)
    name = models.TextField(blank=True)
    selectable = models.BooleanField(default=True)

    class Meta:  # noqa: D101
        abstract = True
        ordering = ('name', )

    def __str__(self):
        """Human readable admin name."""
        return self.name


class BaseOrderedConstantModel(BaseConstantModel):
    """Constants where values are manually ordered (by the order column) when displayed."""

    # Uses a float to make reordering easier
    order = models.FloatField(default=0.0)

    class Meta:  # noqa: D101
        abstract = True
        ordering = ('order', )
