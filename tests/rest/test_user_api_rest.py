from unittest import mock

import pytest
from rest_framework.reverse import reverse

from entities.user import User
from usecases.utils.responses import ResponseSuccess


@pytest.mark.django_db
@mock.patch("usecases.user_signup.user_signup_use_case")
def test_it_creates_a_user_correctly_through_rest_api(use_case_mock, user_data, client):
    use_case_mock.return_value = ResponseSuccess(User(**user_data))
    url = reverse("users-list")
    response = client.post(url, user_data)
    assert response.status_code == 200
