from pydantic import BaseModel
from sqlalchemy import UUID


class GetFullSimStatusQuery(BaseModel):
    sim_id: UUID
