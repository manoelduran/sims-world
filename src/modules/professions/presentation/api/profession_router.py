from fastapi import APIRouter, Depends, status
from typing import List

from src.modules.professions.dependencies import get_profession_controller
from src.modules.professions.presentation.api.profession_controller import (
    ProfessionController,
)
from src.modules.professions.presentation.dto.create_profession_dto import (
    CreateProfessionDto,
)
from src.modules.professions.presentation.response.create_profession_response import (
    CreateProfessionResponse,
)

router = APIRouter()


@router.post(
    "/professions",
    response_model=CreateProfessionResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Adiciona uma nova profissão ao catálogo",
)
def create_profession(
    data: CreateProfessionDto,
    controller: ProfessionController = Depends(get_profession_controller),
):
    return controller.create(data)


@router.get(
    "/professions",
    response_model=List[CreateProfessionResponse],
    summary="Lista todas as profissões disponíveis",
)
def list_professions(
    controller: ProfessionController = Depends(get_profession_controller),
):
    return controller.get_all()
