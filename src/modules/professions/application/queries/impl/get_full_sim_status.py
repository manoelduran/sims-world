from pydantic import BaseModel
from uuid import UUID


class GetFullSimStatusQuery(BaseModel):
    sim_id: UUID
