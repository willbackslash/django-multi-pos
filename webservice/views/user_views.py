from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from multipos.utils.user_serializer import UserSerializer, CreateUserSerializer
from repositories.users_repository import UserRepository
from usecases.user_signup import user_signup_use_case, build_signup_request
from webservice.models import User
from webservice.permissions import UserCanCreateUsers
from webservice.status_codes import STATUS_CODES


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [UserCanCreateUsers]
    repository = UserRepository(User)

    # just to have the right schema on the /docs
    def get_serializer_class(self):
        if self.action == "create":
            return CreateUserSerializer

        return self.serializer_class

    def create(self, request, *args, **kwargs):
        params = {
            "username": request.data.get("username"),
            "email": request.data.get("email"),
            "password": request.data.get("password"),
        }
        use_case_request = build_signup_request(params)
        use_case_response = user_signup_use_case(self.repository, use_case_request)
        # branch = Branch.objects.get(pk=cleaned_data["branch_id"])
        # BranchUser(user=user, branch=branch)

        return Response(
            use_case_response.value.dict()
            if use_case_response
            else use_case_response.message,
            STATUS_CODES[use_case_response.type],
        )
