from fastapi import Depends
from sqlalchemy.orm import Session
from src.modules.professions.application.commands.handlers.create_profession_handler import (
    CreateProfessionHandler,
)
from src.modules.professions.application.queries.handlers.get_all_professions import (
    GetAllProfessionsHandler,
)
from src.core.database import get_db

from .application.ports.i_profession_repository import IProfessionRepository
from .infrastructure.persistence.postgres_profession_repository import (
    PostgresProfessionRepository,
)

from .presentation.api.profession_controller import ProfessionController


def get_profession_repository(db: Session = Depends(get_db)) -> IProfessionRepository:
    return PostgresProfessionRepository(db_session=db)


def get_create_profession_handler(
    repo: IProfessionRepository = Depends(get_profession_repository),
) -> CreateProfessionHandler:
    return CreateProfessionHandler(repository=repo)


def get_all_professions_handler(
    repo: IProfessionRepository = Depends(get_profession_repository),
) -> GetAllProfessionsHandler:
    return GetAllProfessionsHandler(repository=repo)


def get_profession_controller(
    create_handler: CreateProfessionHandler = Depends(get_create_profession_handler),
    get_all_handler: GetAllProfessionsHandler = Depends(get_all_professions_handler),
) -> ProfessionController:
    return ProfessionController(
        create_handler=create_handler, get_all_handler=get_all_handler
    )
