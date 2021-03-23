from unittest.mock import Mock

import pytest

from entities.user import User
from repositories.users_repository import UserRepository


@pytest.fixture()
def user_data():
    return {
        "id": 1,
        "email": "test@example.com",
        "password": "secret",
        "username": "john1992",
        "first_name": "John",
        "last_name": "Doe",
        "is_staff": False,
        "is_superuser": False,
        "is_active": True,
    }


@pytest.fixture
def user(user_data):
    return User(**user_data)


@pytest.fixture
def dummy_user_repo(user):
    mocked_repo = Mock(spec=UserRepository)
    mocked_repo.create_user.return_value = user
    return mocked_repo
