from sqlalchemy.orm import Session
from uuid import UUID
from typing import List, Optional
from ...domain.entities.sim import Sim
from ...application.ports.i_sim_repository import ISimRepository
from .sim_model import SimModel

class PostgresSimRepository(ISimRepository):
    def __init__(self, db_session: Session):
        self._db = db_session

    def save(self, sim: Sim) -> Sim:
        sim_model = SimModel(**sim.model_dump())

        self._db.add(sim_model)
        self._db.commit()
        self._db.refresh(sim_model)

        return Sim.model_validate(sim_model)

    def find_by_id(self, id: UUID) -> Optional[Sim]:
        sim_model = self._db.query(SimModel).filter(SimModel.id == id).first()
        if sim_model:
            return Sim.model_validate(sim_model)
        return None

    def find_by_personality(self, personality: str) -> List[Sim]:
        return []