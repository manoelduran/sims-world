from pydantic import BaseModel


class CreateSimCommand(BaseModel):
    name: str
    personality: str
