from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password"]


class CreateUserSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=1, allow_null=False)
    password = serializers.CharField(min_length=4, allow_null=False)
    branch_id = serializers.UUIDField(allow_null=False)
