from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class Meta:
        db_table = "users"
        permissions = [
            ("can_create_users_for_his_branch", "Can create users for his branch"),
            (
                "can_create_users_for_his_company",
                "Can create users for his company on any branch",
            ),
        ]
