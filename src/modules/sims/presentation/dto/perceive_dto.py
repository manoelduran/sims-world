from pydantic import BaseModel


class PerceiveDto(BaseModel):
    perception: str
