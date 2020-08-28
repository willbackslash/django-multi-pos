from rest_framework.test import APITestCase

from branches.models import BranchUser
from branches.tests.factories.branch_factory import BranchFactory
from branches.tests.factories.branch_user_factory import BranchUserFactory


class TestUserCreation(APITestCase):
    def setUp(self) -> None:
        self.branch_user = BranchUserFactory()
        self.other_company_branch = BranchFactory()

    def test_user_doesnt_belong_to_the_other_company(self):
        user = BranchUser.objects.filter(
            branch=self.other_company_branch, user=self.branch_user.user
        ).first()
        self.assertIsNone(user)

    def test_given_a_user_from_a_company_then_can_not_create_users_for_other_company(
        self,
    ):
        pass
