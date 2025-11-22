from pydantic import BaseModel


class CreateProfessionCommand(BaseModel):
    name: str
    base_salary: int
    education_required: str
