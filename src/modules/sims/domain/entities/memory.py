from pydantic import BaseModel
from uuid import UUID


class Memory(BaseModel):
    id: UUID
    description: str
    importance_score: int

    class Config:
        from_attributes = True
