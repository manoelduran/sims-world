from pydantic import BaseModel
from sqlalchemy import UUID


class GetSimByIdResponse(BaseModel):
    sim_id: UUID
    name: str
    personality: str
