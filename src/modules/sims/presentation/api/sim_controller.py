from modules.sims.application.commands.handlers.create_sim_handler import (
    CreateSimHandler,
)
from modules.sims.application.commands.impl.create_sim import CreateSimCommand
from modules.sims.application.queries.handlers.get_sim_by_id_handler import (
    GetSimByIdHandler,
)
from modules.sims.application.queries.impl.get_sim_by_id import GetSimByIdQuery
from modules.sims.presentation.dto.create_sim_dto import CreateSimDto
from modules.sims.presentation.dto.get_sim_by_id_dto import GetSimByIdDto
from modules.sims.presentation.response.create_sim_response import CreateSimResponse
from modules.sims.presentation.response.get_sim_by_id_response import GetSimByIdResponse


class SimController:
    def __init__(
        self,
        create_sim_handler: CreateSimHandler,
        get_sim_by_id_handler: GetSimByIdHandler,
    ):
        self.create_sim_handler = create_sim_handler
        self.get_sim_by_id_handler = get_sim_by_id_handler

    def create_new_sim(self, sim_data: CreateSimDto) -> CreateSimResponse:
        command = CreateSimCommand(name=sim_data.name, personality=sim_data.personality)

        created_sim_entity = self.create_sim_handler.handle(command)

        return CreateSimResponse.model_validate(created_sim_entity)

    def get_sim_by_id(self, sim_data: GetSimByIdDto) -> GetSimByIdResponse:
        query = GetSimByIdQuery(sim_id=sim_data.sim_id)
        sim_entity = self.get_sim_by_id_handler.handle(query)
        return GetSimByIdResponse.model_validate(sim_entity)
