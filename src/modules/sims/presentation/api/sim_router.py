from fastapi import APIRouter, Depends, Request, status


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
)
from src.modules.sims.application.commands.handlers.create_sim_handler import (
    CreateSimHandler,
)
from src.modules.sims.presentation.exceptions import sim_not_found_exception_handler
from src.modules.sims.application.exceptions.application_exceptions import (
    SimNotFoundError,
)

from .sim_controller import SimController


router = APIRouter()


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
    sim_data: GetSimByIdDto = Depends(),
    controller: SimController = Depends(get_sim_controller),
):
    return controller.get_sim_by_id(sim_data=sim_data)
