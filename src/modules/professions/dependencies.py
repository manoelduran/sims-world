from fastapi import Depends
from sqlalchemy.orm import Session
from src.modules.sims.application.commands.handlers.run_sim_decision_cycle_handler import (
    RunSimDecisionCycleHandler,
)
from src.modules.sims.application.ports.i_llm_service import ILLMService
from src.modules.sims.infrastructure.adapters.gemini_llm_adapter import GeminiLLMAdapter
from src.modules.sims.application.ports.i_sim_repository import ISimRepository
from src.modules.sims.infrastructure.persistence.postgres_sim_repository import (
    PostgresSimRepository,
)
from src.modules.sims.application.commands.handlers.create_sim_handler import (
    CreateSimHandler,
)
from src.modules.sims.application.queries.handlers.get_full_sim_status_handler import (
    GetFullSimStatusHandler,
)
from src.core.database import get_db


def get_llm_service() -> ILLMService:
    return GeminiLLMAdapter()


def get_sim_repository(db: Session = Depends(get_db)) -> ISimRepository:
    return PostgresSimRepository(db_session=db)


def get_create_sim_handler(
    repository: ISimRepository = Depends(get_sim_repository),
) -> CreateSimHandler:
    return CreateSimHandler(sim_repository=repository)


def get_get_sim_by_id_handler(
    repository: ISimRepository = Depends(get_sim_repository),
) -> GetFullSimStatusHandler:
    return GetFullSimStatusHandler(sim_repository=repository)


def get_run_sim_decision_cycle_handler(
    repository: ISimRepository = Depends(get_sim_repository),
    llm_service: ILLMService = Depends(get_llm_service),
) -> RunSimDecisionCycleHandler:
    return RunSimDecisionCycleHandler(
        sim_repository=repository, llm_service=llm_service
    )
