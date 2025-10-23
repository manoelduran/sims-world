from abc import abstractmethod
from typing import Optional
from uuid import UUID
from modules.sims.domain.entities.needs import SimNeeds
from shared.domain.repositories.i_generic_repository import IGenericRepository
from ...domain.entities.sim import Sim


class ISimRepository(IGenericRepository[Sim]):
    @abstractmethod
    def find_full_by_id(self, sim_id: UUID) -> Optional[Sim]: ...

    @abstractmethod
    def update_needs(self, sim_id: UUID, needs: SimNeeds) -> Optional[SimNeeds]: ...
