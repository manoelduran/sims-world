from pydantic import BaseModel
from uuid import UUID


class SetProfessionDto(BaseModel):
    profession_id: UUID
