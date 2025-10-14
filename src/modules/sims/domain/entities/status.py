from pydantic import BaseModel
from typing import Optional


class SimStatus(BaseModel):
    current_feeling: Optional[str] = None
    current_action: Optional[str] = None
