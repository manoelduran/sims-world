from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List
from .city import City


class GameWorld(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    cities: List[City] = []

    class Config:
        from_attributes = True
