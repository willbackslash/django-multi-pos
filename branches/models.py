import uuid

from django.db import models

from multipos.utils.model_mixins import TimeStampedModel


class Company(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    commercial_name = models.CharField(max_length=255, null=False)
    legal_name = models.CharField(max_length=255, null=False)
    tax_regime = models.CharField(max_length=255, null=True)
    tax_id = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "companies"
        verbose_name_plural = "Companies"


class Branch(TimeStampedModel, models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "branches"
        verbose_name_plural = "Branches"
