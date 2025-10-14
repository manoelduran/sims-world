from pydantic import BaseModel
from sqlalchemy import UUID


class CreateSimCommand(BaseModel):
    name: str
    personality: str
    world_id: UUID
