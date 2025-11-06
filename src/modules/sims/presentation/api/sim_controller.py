from uuid import UUID
from src.modules.sims.application.commands.impl.run_sim_decision_cycle import (
    RunSimDecisionCycleCommand,
)
from src.modules.sims.presentation.dto.perceive_dto import PerceiveDto
from src.modules.sims.presentation.response.action_response import ActionResponse
from src.modules.sims.application.commands.handlers.run_sim_decision_cycle_handler import (
    RunSimDecisionCycleHandler,
)
from src.modules.sims.application.commands.handlers.create_sim_handler import (
    CreateSimHandler,
)
from src.modules.sims.application.commands.impl.create_sim import CreateSimCommand
from src.modules.sims.application.queries.handlers.get_sim_by_id_handler import (
    GetSimByIdHandler,
)
from src.modules.sims.application.queries.impl.get_sim_by_id import GetSimByIdQuery
from src.modules.sims.presentation.dto.create_sim_dto import CreateSimDto
from src.modules.sims.presentation.dto.get_sim_by_id_dto import GetSimByIdDto
from src.modules.sims.presentation.response.create_sim_response import CreateSimResponse
from src.modules.sims.presentation.response.get_sim_by_id_response import (
    GetSimByIdResponse,
)


class SimController:
    def __init__(
        self,
        create_sim_handler: CreateSimHandler,
        get_sim_by_id_handler: GetSimByIdHandler,
        run_decision_cycle_handler: RunSimDecisionCycleHandler,
    ):
        self.create_sim_handler = create_sim_handler
        self.get_sim_by_id_handler = get_sim_by_id_handler
        self.run_decision_cycle_handler = run_decision_cycle_handler

    def create_new_sim(self, sim_data: CreateSimDto) -> CreateSimResponse:
        command = CreateSimCommand(
            name=sim_data.name,
            personality=sim_data.personality,
        )

        created_sim_entity = self.create_sim_handler.handle(command)

        return CreateSimResponse.model_validate(created_sim_entity)

    def get_sim_by_id(self, sim_data: GetSimByIdDto) -> GetSimByIdResponse:
        query = GetSimByIdQuery(sim_id=sim_data.sim_id)
        sim_entity = self.get_sim_by_id_handler.handle(query)
        return GetSimByIdResponse.model_validate(sim_entity)

    def perceive_and_act(self, sim_id: UUID, data: PerceiveDto) -> ActionResponse:
        command = RunSimDecisionCycleCommand(sim_id=sim_id, perception=data.perception)
        final_state = self.run_decision_cycle_handler.handle(command)
        return ActionResponse(
            action=final_state.get("action"),
            feeling=final_state.get("feeling"),
            reflection=final_state.get("reflection"),
        )
