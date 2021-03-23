from entities.company import Company, Branch


class CompanyRepositoryBase:
    def create(self, company_name: str):
        raise NotImplemented()

    def create_branch(self, branch_name: str):
        raise NotImplemented()


class CompanyRepository(CompanyRepositoryBase):
    def __init__(self, company_orm_model, branch_orm_model):
        self.__company_orm_model = company_orm_model
        self.__branch_orm_model = branch_orm_model

    def create(self, company_name: str):
        return Company(
            **self.__company_orm_model.objects.create(
                commercial_name=company_name
            ).__dict__
        )

    def create_branch(self, branch_name: str):
        return Branch(
            **self.__branch_orm_model.objects.create(
                commercial_name=branch_name
            ).__dict__
        )
