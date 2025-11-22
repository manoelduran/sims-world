from pydantic import BaseModel


class CreateProfessionDto(BaseModel):
    name: str
    base_salary: int
    education_required: str
