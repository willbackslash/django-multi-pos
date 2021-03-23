from multipos.utils.user_serializer import CreateUserSerializer
from usecases.utils.requests import InvalidRequest, ValidRequest
from usecases.utils.responses import (
    build_response_from_invalid_request,
    ResponseFailure,
    ResponseTypes,
    ResponseSuccess,
)


def build_signup_request(params):
    invalid_req = InvalidRequest()
    serializer = CreateUserSerializer(data=params)
    if not serializer.is_valid():
        for error, exceptions in serializer.errors.items():
            for exception in exceptions:
                invalid_req.add_error(error, exception)
        return invalid_req

    return ValidRequest(params=params)


def user_signup_use_case(users_repository, request):
    if not request:
        return build_response_from_invalid_request(request)

    try:
        return ResponseSuccess(users_repository.create_user(**request.params))
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)


class UserSignupUseCase:
    def __init__(self, users_repository):
        self.__users_repository = users_repository
        self.__params = None

    def set_params(self, params):
        self.__params = params

    def execute(self):
        if not self.__params:
            raise Exception
        return self.__users_repository.create_user(**self.__params)
