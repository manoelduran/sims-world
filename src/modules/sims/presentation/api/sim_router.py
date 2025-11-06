from uuid import UUID
from fastapi import APIRouter, Depends, status
from src.modules.sims.application.commands.handlers.run_sim_decision_cycle_handler import (
    RunSimDecisionCycleHandler,
)
from src.modules.sims.presentation.dto.perceive_dto import PerceiveDto
from src.modules.sims.presentation.response.action_response import ActionResponse
from src.modules.sims.presentation.dto.get_sim_by_id_dto import GetSimByIdDto
from src.modules.sims.presentation.response.get_sim_by_id_response import (
    GetSimByIdResponse,
)
from src.modules.sims.presentation.dto.create_sim_dto import CreateSimDto
from src.modules.sims.presentation.response.create_sim_response import CreateSimResponse
from src.modules.sims.application.queries.handlers.get_sim_by_id_handler import (
    GetSimByIdHandler,
)
from src.modules.sims.dependencies import (
    get_create_sim_handler,
    get_get_sim_by_id_handler,
    get_run_sim_decision_cycle_handler,
)
from src.modules.sims.application.commands.handlers.create_sim_handler import (
    CreateSimHandler,
)
from .sim_controller import SimController


router = APIRouter()


def get_sim_controller(
    create_handler: CreateSimHandler = Depends(get_create_sim_handler),
    get_by_id_handler: GetSimByIdHandler = Depends(get_get_sim_by_id_handler),
    run_decision_handler: RunSimDecisionCycleHandler = Depends(
        get_run_sim_decision_cycle_handler
    ),
) -> SimController:
    return SimController(
        create_sim_handler=create_handler,
        get_sim_by_id_handler=get_by_id_handler,
        run_decision_cycle_handler=run_decision_handler,
    )


@router.post(
    "/sims",
    response_model=CreateSimResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Cria um novo Sim",
)
def create_sim_route(
    sim_data: CreateSimDto, controller: SimController = Depends(get_sim_controller)
):
    return controller.create_new_sim(sim_data)


@router.get(
    "/sims/{sim_id}", response_model=GetSimByIdResponse, summary="Busca um Sim por ID"
)
def get_sim_by_id_route(
    sim_data: GetSimByIdDto = Depends(),
    controller: SimController = Depends(get_sim_controller),
):
    return controller.get_sim_by_id(sim_data=sim_data)


@router.post(
    "/sims/{sim_id}/perceive",
    response_model=ActionResponse,
    summary="Faz o Sim perceber algo e reagir",
)
def sim_perceive_route(
    sim_id: UUID,
    data: PerceiveDto,
    controller: SimController = Depends(get_sim_controller),
):
    return controller.perceive_and_act(sim_id, data)
