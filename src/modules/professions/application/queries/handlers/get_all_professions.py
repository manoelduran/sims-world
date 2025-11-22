from typing import List

from src.modules.professions.application.ports.i_profession_repository import (
    IProfessionRepository,
)
from src.modules.professions.domain.profession import Profession


class GetAllProfessionsHandler:
    def __init__(self, repository: IProfessionRepository):
        self.repository = repository

    def handle(self) -> List[Profession]:
        return self.repository.find_all()
