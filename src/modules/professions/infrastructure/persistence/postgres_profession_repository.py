from sqlalchemy.orm import Session
from typing import List, Optional
from uuid import UUID

from src.modules.professions.domain.profession import Profession
from src.modules.professions.infrastructure.persistence.profession_model import (
    ProfessionModel,
)

from ...application.ports.i_profession_repository import IProfessionRepository


class PostgresProfessionRepository(IProfessionRepository):
    def __init__(self, db_session: Session):
        self._db = db_session

    def save(self, profession: Profession) -> Profession:
        # Mapeia Entidade -> Modelo
        profession_model = ProfessionModel(**profession.model_dump())

        self._db.add(profession_model)
        self._db.commit()
        self._db.refresh(profession_model)

        # Mapeia Modelo -> Entidade
        return Profession.model_validate(profession_model)

    def find_all(self) -> List[Profession]:
        models = self._db.query(ProfessionModel).all()
        return [Profession.model_validate(m) for m in models]

    def find_by_id(self, id: UUID) -> Optional[Profession]:
        model = self._db.query(ProfessionModel).filter(ProfessionModel.id == id).first()
        if model:
            return Profession.model_validate(model)
        return None
