from sqlalchemy.orm import Session, joinedload
from uuid import UUID
from typing import Optional

from src.modules.sims.domain.entities.relationship import Relationship
from src.modules.sims.infrastructure.persistence.needs_model import SimNeedsModel
from src.modules.sims.infrastructure.persistence.relationship_model import (
    RelationshipModel,
)
from src.modules.sims.infrastructure.persistence.sim_model import SimModel
from src.modules.sims.infrastructure.persistence.status_model import SimStatusModel
from src.modules.sims.infrastructure.persistence.skill_model import SkillModel
from src.modules.sims.infrastructure.persistence.memory_models import MemoryModel
from ...domain.entities.sim import Sim
from ...domain.entities.needs import SimNeeds
from ...application.ports.i_sim_repository import ISimRepository


class PostgresSimRepository(ISimRepository):
    def __init__(self, db_session: Session):
        self._db = db_session

    def save(self, entity: Sim) -> Sim:
        sim_data = entity.model_dump(
            exclude={"needs", "status", "skills", "relationships", "memories"}
        )

        sim_model = SimModel(**sim_data)
        sim_model.needs = SimNeedsModel(**entity.needs.model_dump())
        sim_model.status = SimStatusModel(**entity.status.model_dump())

        self._db.add(sim_model)
        self._db.commit()

        return self.find_full_by_id(sim_model.id)

    def find_full_by_id(self, sim_id: UUID) -> Optional[Sim]:
        sim_model = (
            self._db.query(SimModel)
            .options(
                joinedload(SimModel.needs),
                joinedload(SimModel.status),
                joinedload(SimModel.skills),
                # Eager loading de relacionamentos e memórias pode ser pesado,
                # mas para um único Sim é geralmente aceitável.
                joinedload(SimModel.memories),
            )
            .filter(SimModel.id == sim_id)
            .first()
        )
        if not sim_model:
            return None

        # Relações precisam ser carregadas e mapeadas com cuidado
        relationships_model = (
            self._db.query(RelationshipModel)
            .filter(
                (RelationshipModel.sim_a_id == sim_id)
                | (RelationshipModel.sim_b_id == sim_id)
            )
            .all()
        )

        sim_entity = Sim.model_validate(sim_model)

        for rel in relationships_model:
            target_id = (
                rel.sim_b_id if str(rel.sim_a_id) == str(sim_id) else rel.sim_a_id
            )
            relationship_entity = Relationship(
                target_sim_id=target_id,
                relationship_score=rel.relationship_score,
                romance_score=rel.romance_score,
                commitment_level=rel.commitment_level,
            )
            sim_entity.relationships.append(relationship_entity)

        return sim_entity

    def update_needs(self, sim_id: UUID, needs: SimNeeds) -> Optional[SimNeeds]:
        needs_model = (
            self._db.query(SimNeedsModel).filter(SimNeedsModel.sim_id == sim_id).first()
        )
        if not needs_model:
            return None

        needs_model.hunger = needs.hunger
        needs_model.energy = needs.energy
        needs_model.social = needs.social
        needs_model.hygiene = needs.hygiene

        self._db.commit()
        self._db.refresh(needs_model)

        return SimNeeds.model_validate(needs_model)

    def find_by_id(self, id: UUID) -> Optional[Sim]:
        return self.find_full_by_id(id)
