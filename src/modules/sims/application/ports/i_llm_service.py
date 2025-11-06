from abc import ABC, abstractmethod
from typing import List, Dict, Any


class ILLMService(ABC):
    @abstractmethod
    def invoke(self, prompt: str) -> str: ...

    @abstractmethod
    def invoke_json(self, prompt: str) -> Dict[str, Any]: ...

    @abstractmethod
    def generate_embedding(self, text: str) -> List[float]: ...
