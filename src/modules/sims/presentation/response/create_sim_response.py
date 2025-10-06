from pydantic import BaseModel
from uuid import UUID

class CreateSimResponse(BaseModel):
    id: UUID
    name: str
    personality: str