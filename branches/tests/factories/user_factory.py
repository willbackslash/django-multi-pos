import factory

from users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("first_name")
    email = factory.Faker("email")
    password = factory.Faker("password", length=12)

    class Params:
        admin = factory.Trait(is_staff=True)
        super_user = factory.Trait(is_superuser=True)
