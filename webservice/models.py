import uuid

from django.db import models

from django.contrib.auth.models import AbstractUser
from multipos.utils.model_mixins import TimeStampedModel


class User(AbstractUser):
    class Meta:
        db_table = "users"
        permissions = [
            ("can_create_users_for_his_branch", "Can create users for his branch"),
            (
                "can_create_users_for_his_company",
                "Can create users for his company on any branch",
            ),
        ]


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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False)

    class Meta:
        db_table = "branches"
        verbose_name_plural = "Branches"


class BranchUser(TimeStampedModel, models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = (("branch", "user"),)
        db_table = "branch_users"


class CompanyBrand(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = "company_brands"
        verbose_name_plural = "Company Brands"


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
        verbose_name_plural = "Company Items"


class BranchItem(TimeStampedModel, models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cost = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    price = models.DecimalField(max_digits=12, decimal_places=2, null=False)
    stock = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    item = models.ForeignKey(CompanyItem, on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)

    class Meta:
        db_table = "branch_items"
        verbose_name_plural = "Branch Items"
