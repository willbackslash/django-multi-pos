from usecases.user_signup import build_signup_request, user_signup_use_case
from usecases.utils.responses import ResponseTypes


def test_signup_use_case_without_user_data(dummy_user_repo):
    request = build_signup_request({})
    assert bool(request) is False
    response = user_signup_use_case(dummy_user_repo, request)
    assert bool(response) is False
    assert response.type == ResponseTypes.PARAMETERS_ERROR
    assert response.value == {
        "message": "email: This field is required.\npassword: This field is required.",
        "type": "ParameterError",
    }


def test_given_a_new_user_it_signups_correctly(user_data, dummy_user_repo):
    request = build_signup_request(user_data)
    response = user_signup_use_case(dummy_user_repo, request)
    assert bool(response) is True
    assert response.type == ResponseTypes.SUCCESS
    user = response.value.dict()
    assert user["email"] == user_data["email"]
    assert user["username"] == user_data["username"]
    assert user["is_active"] is True


def test_given_a_db_error_cant_create_user_it_cant_creat_user(
    user_data, dummy_user_repo
):
    dummy_user_repo.create_user.side_effect = Exception("db error")
    request = build_signup_request(user_data)
    response = user_signup_use_case(dummy_user_repo, request)
    assert bool(response) is False
    assert response.value == {"type": "SystemError", "message": "Exception: db error"}
    assert response.type == ResponseTypes.SYSTEM_ERROR
