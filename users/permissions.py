from rest_framework.permissions import BasePermission

from branches.models import BranchUser, Branch


class UserBelongsToCompany(BasePermission):
    """
    Allows access only to customer users with qualified account.
    """

    def has_permission(self, request, view):
        user = request.user
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

        return bool(user and user.is_authenticated and not user.is_staff)
