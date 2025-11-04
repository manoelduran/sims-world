from pydantic import BaseModel


class SimNeeds(BaseModel):
    hunger: int
    energy: int
    social: int
    hygiene: int

    class Config:
        from_attributes = True
