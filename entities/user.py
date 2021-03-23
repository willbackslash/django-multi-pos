from pydantic.main import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    first_name: str
    last_name: str
    is_staff: bool
    is_superuser: bool
    is_active: bool
