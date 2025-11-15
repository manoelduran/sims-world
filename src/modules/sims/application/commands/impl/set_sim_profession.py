from pydantic import BaseModel
from uuid import UUID


class SetSimProfessionCommand(BaseModel):
    sim_id: UUID
    profession_id: UUID
