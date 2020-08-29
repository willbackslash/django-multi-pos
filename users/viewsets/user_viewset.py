from rest_framework import viewsets, status
from rest_framework.response import Response

from branches.models import Branch, BranchUser
from multipos.utils.user_serializer import UserSerializer, CreateUserSerializer
from users.models import User
from users.permissions import UserBelongsToCompany


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [UserBelongsToCompany]

    def create(self, request, *args, **kwargs):
        create_user_serializer = CreateUserSerializer(data=request.data)

        if not create_user_serializer.is_valid():
            return Response("Bad request", status.HTTP_400_BAD_REQUEST)

        cleaned_data = create_user_serializer.data
        user = User(
            username=cleaned_data["email"],
            email=cleaned_data["email"],
            password=cleaned_data["password"],
        )
        branch = Branch.objects.get(pk=cleaned_data["branch_id"])
        BranchUser(user=user, branch=branch)

        return Response("OK", status.HTTP_201_CREATED)
