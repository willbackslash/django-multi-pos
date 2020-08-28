import factory

from branches.models import Company


class CompanyFactory(factory.django.DjangoModelFactory):
    commercial_name = factory.Faker("company")
    legal_name = factory.Faker("company")

    class Meta:
        model = Company
