from uuid import UUID
from pydantic import BaseModel


class GetSimByIdResponse(BaseModel):
    id: UUID
    name: str
    personality_summary: str

    class Config:
        from_attributes = True
