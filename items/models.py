import uuid

from django.db import models

from branches.models import Company
from multipos.utils.model_mixins import TimeStampedModel


class CompanyBrand(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = "company_brands"
        verbose_name_plural = "company_brands"


class CompanyItem(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    sku = models.CharField(max_length=16, null=False)
    model = models.CharField(max_length=255, null=False)
    brand = models.ForeignKey(CompanyBrand, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, null=True)
    subcategory = models.CharField(max_length=255, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["category", "subcategory"]),
        ]
        db_table = "company_items"


class BranchItemPrice(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(CompanyItem, on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=False)

    class Meta:
        db_table = "branch_item_prices"
