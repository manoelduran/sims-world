from pydantic import BaseModel


class ActionResponse(BaseModel):
    action: str
    feeling: str
    reflection: str
