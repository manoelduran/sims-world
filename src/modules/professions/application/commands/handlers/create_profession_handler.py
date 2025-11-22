from src.modules.professions.application.commands.impl.create_profession import (
    CreateProfessionCommand,
)
from src.modules.professions.application.ports.i_profession_repository import (
    IProfessionRepository,
)
from src.modules.professions.domain.profession import Profession


class CreateProfessionHandler:
    def __init__(self, repository: IProfessionRepository):
        self.repository = repository

    def handle(self, command: CreateProfessionCommand) -> Profession:
        profession = Profession(
            name=command.name,
            base_salary=command.base_salary,
            education_required=command.education_required,
        )
        return self.repository.save(profession)
