from uuid import UUID
from pydantic import BaseModel


class CreateProfessionResponse(BaseModel):
    id: UUID
    name: str
    base_salary: int
    education_required: str

    class Config:
        from_attributes = True
