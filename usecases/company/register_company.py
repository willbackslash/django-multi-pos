from usecases.utils.responses import (
    ResponseFailure,
    ResponseTypes,
    ResponseSuccess,
    build_response_from_invalid_request,
)


def register_company_use_case(request, company_repository):
    """
    This function registers a new company and its initial branches
    request.params = {
        "company_name": "Buggysoft Inc.",
        "branches": [
            "store1",
            "store2",
            "store3"
        ]
    }
    """

    if not request:
        return build_response_from_invalid_request(request)

    try:
        params = request.params
        company = company_repository.create(company_name=params.get("company_name"))

        for branch in params.get("branches"):
            company_repository.create_branch(company, branch)

        return ResponseSuccess(company)
    except Exception as exc:
        return ResponseFailure(ResponseTypes.SYSTEM_ERROR, exc)
