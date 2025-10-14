from pydantic import BaseModel
from typing import Optional
from uuid import UUID


class Relationship(BaseModel):
    target_sim_id: UUID
    relationship_score: int
    romance_score: int
    commitment_level: Optional[str] = None
