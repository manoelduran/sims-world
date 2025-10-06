from uuid import UUID
from pydantic import BaseModel


class GetSimByIdQuery(BaseModel):
    sim_id: UUID
