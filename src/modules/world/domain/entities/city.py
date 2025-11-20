from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List
from .neighborhood import Neighborhood


class City(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    neighborhoods: List[Neighborhood] = []

    class Config:
        from_attributes = True
