from fastapi import APIRouter, Depends, status
from modules.sims.application.commands.handlers.create_sim_handler import (
    CreateSimHandler,
)
from modules.sims.application.exceptions.application_exceptions import SimNotFoundError
from modules.sims.application.queries.handlers.get_sim_by_id_handler import (
    GetSimByIdHandler,
)
from modules.sims.presentation.dto.create_sim_dto import CreateSimDto
from modules.sims.presentation.dto.get_sim_by_id_dto import GetSimByIdDto
from modules.sims.presentation.exceptions import sim_not_found_exception_handler
from modules.sims.presentation.response.create_sim_response import CreateSimResponse
from modules.sims.presentation.response.get_sim_by_id_response import GetSimByIdResponse
from .sim_controller import SimController
from ...dependencies import get_create_sim_handler, get_get_sim_by_id_handler

router = APIRouter(
    exception_handlers={SimNotFoundError: sim_not_found_exception_handler}
)


def get_sim_controller(
    create_handler: CreateSimHandler = Depends(get_create_sim_handler),
    get_by_id_handler: GetSimByIdHandler = Depends(get_get_sim_by_id_handler),
) -> SimController:
    return SimController(
        create_sim_handler=create_handler, get_sim_by_id_handler=get_by_id_handler
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
    sim_data: GetSimByIdDto, controller: SimController = Depends(get_sim_controller)
):
    return controller.get_sim_by_id(sim_id=sim_data.sim_id)
