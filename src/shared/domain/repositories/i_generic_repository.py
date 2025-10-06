from abc import ABC, abstractmethod
from typing import TypeVar, Generic
from uuid import UUID

T = TypeVar("T")


class IGenericRepository(ABC, Generic[T]):
    @abstractmethod
    def find_by_id(self, id: UUID) -> T | None:
        pass

    @abstractmethod
    def save(self, entity: T) -> T:
        pass
