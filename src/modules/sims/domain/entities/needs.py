from pydantic import BaseModel


class SimNeeds(BaseModel):
    hunger: int
    energy: int
    social: int
    hygiene: int
