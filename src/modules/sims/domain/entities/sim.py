from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import List, Optional
from .needs import SimNeeds
from .status import SimStatus
from .skill import Skill
from .relationship import Relationship
from .memory import Memory


class Sim(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    personality_summary: Optional[str] = None

    age_in_days: int
    life_stage: str
    is_alive: bool

    needs: SimNeeds
    status: SimStatus
    skills: List[Skill] = []

    relationships: List[Relationship] = []
    memories: List[Memory] = []

    class Config:
        from_attributes = True
