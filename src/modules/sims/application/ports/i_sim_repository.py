from abc import abstractmethod
from typing import List, Optional
from uuid import UUID

from src.modules.sims.domain.entities.memory import Memory
from src.modules.sims.domain.entities.status import SimStatus
from src.modules.sims.infrastructure.persistence.action_log_model import ActionLogModel
from ...domain.entities.needs import SimNeeds
from src.shared.domain.repositories.i_generic_repository import IGenericRepository
from ...domain.entities.sim import Sim


class ISimRepository(IGenericRepository[Sim]):
    @abstractmethod
    def find_full_by_id(self, sim_id: UUID) -> Optional[Sim]: ...

    @abstractmethod
    def update_needs(self, sim_id: UUID, needs: SimNeeds) -> Optional[SimNeeds]: ...

    @abstractmethod
    def add_memory(
        self, sim_id: UUID, description: str, importance: int, embedding: List[float]
    ) -> Memory: ...

    @abstractmethod
    def find_relevant_memories(
        self, sim_id: UUID, embedding: List[float], k: int = 5
    ) -> List[Memory]: ...

    @abstractmethod
    def get_short_term_memory(
        self, sim_id: UUID, k: int = 5
    ) -> List[ActionLogModel]: ...

    @abstractmethod
    def save_action_to_log(
        self, sim_id: UUID, action_type: str, description: str
    ) -> ActionLogModel: ...

    @abstractmethod
    def update_sim_status(
        self, sim_id: UUID, feeling: str, action: str
    ) -> SimStatus: ...
