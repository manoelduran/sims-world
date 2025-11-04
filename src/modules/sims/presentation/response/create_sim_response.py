from pydantic import BaseModel
from uuid import UUID


class CreateSimResponse(BaseModel):
    id: UUID
    name: str
    personality_summary: str

    class Config:
        from_attributes = True
