from pydantic import BaseModel, Field
from uuid import UUID, uuid4


class Profession(BaseModel):
    id: UUID = Field(default_factory=uuid4)
    name: str
    base_salary: int
    education_required: str  # Ex: 'ensino_medio', 'faculdade'
    # Poderíamos adicionar: skill_required: str (ex: 'logica:5')

    class Config:
        from_attributes = True
