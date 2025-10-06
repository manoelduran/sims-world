from fastapi import Depends
from sqlalchemy.orm import Session
from modules.sims.application.queries.handlers.get_sim_by_id_handler import GetSimByIdHandler
from src.core.database import get_db
from .application.ports.i_sim_repository import ISimRepository
from .infrastructure.persistence.postgres_sim_repository import PostgresSimRepository
from .application.commands.impl.create_sim import CreateSimHandler

def get_sim_repository(db: Session = Depends(get_db)) -> ISimRepository:

    return PostgresSimRepository(db_session=db)

def get_create_sim_handler(
    repository: ISimRepository = Depends(get_sim_repository),
) -> CreateSimHandler:
    return CreateSimHandler(sim_repository=repository)

def get_get_sim_by_id_handler(
    repository: ISimRepository = Depends(get_sim_repository),
) -> GetSimByIdHandler:
    return GetSimByIdHandler(sim_repository=repository)