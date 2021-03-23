from usecases.utils.requests import InvalidRequest


class ResponseTypes:
    PARAMETERS_ERROR = "ParameterError"
    RESOURCE_ERROR = "ResourceError"
    SYSTEM_ERROR = "SystemError"
    SUCCESS = "Success"


class ResponseFailure:
    def __init__(self, type, message):
        self.type = type
        self.message = self.format_message(message)

    @staticmethod
    def format_message(message):
        if isinstance(message, Exception):
            return "{}: {}".format(message.__class__.__name__, "{}".format(message))
        return message

    @property
    def value(self):
        return {"type": self.type, "message": self.message}

    def __bool__(self):
        return False


class ResponseSuccess:
    def __init__(self, value=None):
        self.type = ResponseTypes.SUCCESS
        self.value = value

    def __bool__(self):
        return True


def build_response_from_invalid_request(invalid_request: InvalidRequest):
    message = "\n".join(
        [
            "{}: {}".format(err["parameter"], err["message"])
            for err in invalid_request.errors
        ]
    )

    return ResponseFailure(ResponseTypes.PARAMETERS_ERROR, message)
