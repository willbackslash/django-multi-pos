from django.contrib.auth.models import Group
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from branches.models import BranchUser
from branches.tests.factories.branch_factory import BranchFactory
from branches.tests.factories.branch_user_factory import BranchUserFactory


class TestUserCreation(APITestCase):
    def setUp(self) -> None:
        self.create_users_url = reverse("users-list")
        self.branch_user = BranchUserFactory()
        self.user_company_other_branch = BranchFactory(
            company=self.branch_user.branch.company
        )
        self.other_company_branch = BranchFactory()
        self.client.force_login(self.branch_user.user)
        self.master_company_user_group = Group.objects.get(
            name__exact="company_master_user"
        )
        self.master_branch_user_group = Group.objects.get(
            name__exact="branch_master_user"
        )

    def test_user_doesnt_belong_to_the_other_company(self):
        user = BranchUser.objects.filter(
            branch=self.other_company_branch, user=self.branch_user.user
        ).first()
        self.assertIsNone(user)

    def test_given_a_user_from_a_company_then_can_not_create_users_for_other_company(
        self,
    ):
        self.branch_user.user.groups.add(self.master_company_user_group)
        payload = {
            "email": "test@mail.com",
            "password": "secret",
            "branch_id": str(self.other_company_branch.id),
        }
        with self.assertRaises(
            Exception
        ):  # TODO: Change for specific exceptions instead using this generic
            try:
                response = self.client.post(self.create_users_url, payload)
                self.assertEquals(response.status_code, 500)
            except Exception as e:
                self.assertEquals(e.value, "user_doesnt_belong_to_the_company")

    def test_given_a_user_from_a_branch_then_can_create_a_user_for_his_own_branch(self):
        self.branch_user.user.groups.add(self.master_branch_user_group)
        payload = {
            "email": "test@mail.com",
            "password": "secret",
            "branch_id": str(self.branch_user.branch.id),
        }
        response = self.client.post(self.create_users_url, payload)
        self.assertEquals(response.status_code, 201)
        self.assertEquals(response.content, b'"OK"')

    def test_given_a_master_branch_user_then_can_not_create_a_user_for_another_branch_of_his_company(
        self,
    ):
        self.branch_user.user.groups.add(self.master_branch_user_group)
        payload = {
            "email": "test@mail.com",
            "password": "secret",
            "branch_id": str(self.user_company_other_branch.id),
        }
        response = self.client.post(self.create_users_url, payload)
        self.assertEquals(response.status_code, 403)


def test_given_a_master_user_from_a_company_branch_then_can_create_a_user_for_other_company_branch(
    self,
):
    self.branch_user.user.groups.add(self.master_company_user_group)
    payload = {
        "email": "test@mail.com",
        "password": "secret",
        "branch_id": str(self.user_company_other_branch.id),
    }
    response = self.client.post(self.create_users_url, payload)
    self.assertEquals(response.status_code, 201)
    self.assertEquals(response.content, b'"OK"')
