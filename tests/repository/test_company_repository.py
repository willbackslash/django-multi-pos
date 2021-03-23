import pytest

from repositories.company_repository import CompanyRepository
from webservice.models import Company, Branch


@pytest.mark.django_db
def test_create_company():
    repository = CompanyRepository(Company, Branch)
    category = repository.create(company_name="Buggysoft Inc.")
    assert category.commercial_name == "Buggysoft Inc."
    assert category.id
