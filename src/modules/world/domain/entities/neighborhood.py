from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List
from enum import Enum
from .house import House


class SocialClassEnum(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Neighborhood(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    average_social_class: SocialClassEnum
    average_cost_of_living: int
    houses: List[House] = []

    class Config:
        from_attributes = True
