from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional, Dict, Any


class WorldObject(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    object_type: str  # Ex: 'fridge', 'bed'
    state: Optional[Dict[str, Any]] = None  # Ex: {'is_open': True}

    class Config:
        from_attributes = True
