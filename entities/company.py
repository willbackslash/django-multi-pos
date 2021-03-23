from typing import Optional

from pydantic.main import BaseModel
from pydantic.types import UUID4


class Company(BaseModel):
    id: UUID4
    commercial_name: str
    legal_name: Optional[str]
    tax_regime: Optional[str]
    tax_id: Optional[str]


class Branch(BaseModel):
    id: UUID4
    company: Company
    name: str
