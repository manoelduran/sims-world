from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List, Optional
from .room import Room


class House(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: Optional[str] = None
    address: Optional[str] = None
    rooms: List[Room] = []

    class Config:
        from_attributes = True
