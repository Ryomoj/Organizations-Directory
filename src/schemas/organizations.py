from typing import Optional, List

from pydantic import BaseModel


class OrganizationsSchema(BaseModel):
    id: int
    name: str
    phone_numbers: Optional[List[str]]
