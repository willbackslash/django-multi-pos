from rest_framework.permissions import BasePermission

from branches.models import BranchUser, Branch


class UserCanCreateUsers(BasePermission):
    """
    Allows access only to customer users with qualified account.
    """

    @staticmethod
    def user_can_not_create_account_for_other_branches_of_company(
        requested_branch, user_branch, permissions
    ):
        return (
            requested_branch.company.id == user_branch.company.id
            and requested_branch.id != user_branch.id
            and not "users.can_create_users_for_his_company" in permissions
        )

    @staticmethod
    def user_can_not_create_account_for_his_branch(
        requested_branch, user_branch, permissions
    ):
        return (
            requested_branch.id == user_branch.id
            and not "users.can_create_users_for_his_branch" in permissions
        )

    def has_permission(self, request, view):
        user = request.user
        permissions = request.user.get_all_permissions()
        data = request.data
        if bool(user and user.is_authenticated):
            if user.is_staff:
                # The user is staff so is unauthorized to create users for
                raise Exception("staff_user_calling_endpoint")

        requested_branch = Branch.objects.get(pk=data["branch_id"])
        branch_user = BranchUser.objects.get(user=user)
        if not requested_branch:
            raise Exception("branch_doesnt_exist")
        if not branch_user:
            raise Exception("your_user_doesnt_belong_to_any_company")
        if requested_branch.company.id != branch_user.branch.company.id:
            raise Exception("user_doesnt_belong_to_the_company")

        if self.user_can_not_create_account_for_other_branches_of_company(
            requested_branch, branch_user.branch, permissions
        ):
            return False

        if self.user_can_not_create_account_for_his_branch(
            requested_branch, branch_user.branch, permissions
        ):
            return False

        return bool(user and user.is_authenticated and not user.is_staff)
