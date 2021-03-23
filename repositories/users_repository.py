from entities.user import User


class UserRepository:
    def __init__(self, orm_model):
        self.__orm_model = orm_model

    def create_user(self, username, email, password) -> User:
        user = self.__orm_model.objects.create(
            username=username, email=email, password=password
        )
        return User(**user.__dict__)
