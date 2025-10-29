from uuid import UUID
from pydantic import BaseModel


class GetSimByIdResponse(BaseModel):
    sim_id: UUID
    name: str
    personality: str
