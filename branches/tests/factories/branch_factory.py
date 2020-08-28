import factory

from branches.models import Branch
from branches.tests.factories.company_factory import CompanyFactory


class BranchFactory(factory.django.DjangoModelFactory):
    name = factory.Faker("address")
    company = factory.SubFactory(CompanyFactory)

    class Meta:
        model = Branch
