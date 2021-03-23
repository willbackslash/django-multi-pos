import pytest

from repositories.users_repository import UserRepository
from webservice.models import User


@pytest.mark.django_db
def test_create_user(user_data):
    repository = UserRepository(User)
    user = repository.create_user(
        username=user_data["username"],
        email=user_data["email"],
        password=user_data["password"],
    )
    assert user.username == user_data["username"]
    assert user.email == user_data["email"]
    assert user.is_active is True
