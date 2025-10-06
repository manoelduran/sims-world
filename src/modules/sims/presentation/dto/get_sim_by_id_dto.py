from uuid import UUID
from pydantic import BaseModel, Field


class GetSimByIdDto(BaseModel):
    sim_id: UUID = Field(..., description="O ID do Sim a ser buscado.")
