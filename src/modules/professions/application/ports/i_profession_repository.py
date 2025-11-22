from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from src.modules.professions.domain.profession import Profession


class IProfessionRepository(ABC):
    @abstractmethod
    def save(self, profession: Profession) -> Profession:
        """Salva uma nova profissão ou atualiza uma existente."""
        ...

    @abstractmethod
    def find_all(self) -> List[Profession]:
        """Retorna todas as profissões cadastradas."""
        ...

    @abstractmethod
    def find_by_id(self, id: UUID) -> Optional[Profession]:
        """Busca uma profissão pelo ID."""
        ...
