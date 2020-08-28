import factory

from branches.models import BranchUser
from branches.tests.factories.branch_factory import BranchFactory
from branches.tests.factories.user_factory import UserFactory


class BranchUserFactory(factory.django.DjangoModelFactory):
    branch = factory.SubFactory(BranchFactory)
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = BranchUser
