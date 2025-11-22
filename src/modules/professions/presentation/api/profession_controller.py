from typing import List

from src.modules.professions.application.commands.handlers.create_profession_handler import (
    CreateProfessionHandler,
)
from src.modules.professions.application.commands.impl.create_profession import (
    CreateProfessionCommand,
)
from src.modules.professions.application.queries.handlers.get_all_professions import (
    GetAllProfessionsHandler,
)
from src.modules.professions.presentation.dto.create_profession_dto import (
    CreateProfessionDto,
)
from src.modules.professions.presentation.response.create_profession_response import (
    CreateProfessionResponse,
)


class ProfessionController:
    def __init__(
        self,
        create_handler: CreateProfessionHandler,
        get_all_handler: GetAllProfessionsHandler,
    ):
        self.create_handler = create_handler
        self.get_all_handler = get_all_handler

    def create(self, data: CreateProfessionDto) -> CreateProfessionResponse:
        command = CreateProfessionCommand(**data.model_dump())
        profession = self.create_handler.handle(command)
        return CreateProfessionResponse.model_validate(profession)

    def get_all(self) -> List[CreateProfessionResponse]:
        professions = self.get_all_handler.handle()
        return [CreateProfessionResponse.model_validate(p) for p in professions]
