from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List
from .world_object import WorldObject


class Room(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str  # Ex: 'Kitchen', 'Master Bedroom'
    room_type: str
    objects: List[WorldObject] = []

    class Config:
        from_attributes = True
