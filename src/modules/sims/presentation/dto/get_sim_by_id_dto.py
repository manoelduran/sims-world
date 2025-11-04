from uuid import UUID
from pydantic import BaseModel


class GetSimByIdDto(BaseModel):
    sim_id: UUID
