from pydantic import BaseModel
from uuid import UUID


class RunSimDecisionCycleCommand(BaseModel):
    sim_id: UUID
    perception: str
