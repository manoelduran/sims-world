from pydantic import BaseModel, Field

class CreateSimDto(BaseModel):
    name: str = Field(..., min_length=1, description="O nome do Sim.")
    personality: str = Field(..., description="Um breve resumo da personalidade do Sim.")
