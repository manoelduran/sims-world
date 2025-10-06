from abc import abstractmethod
from typing import List
from shared.domain.repositories.i_generic_repository import IGenericRepository
from ...domain.entities.sim import Sim

class ISimRepository(IGenericRepository[Sim]):
    @abstractmethod
    def find_by_personality(self, personality: str) -> List[Sim]:
        ...