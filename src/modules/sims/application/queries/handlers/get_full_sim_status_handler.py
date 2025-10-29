from src.modules.sims.application.ports.i_sim_repository import ISimRepository
from ...exceptions.application_exceptions import SimNotFoundError
from uuid import UUID
from src.modules.sims.application.queries.impl.get_full_sim_status import (
    GetFullSimStatusQuery,
)
from src.modules.sims.domain.entities.sim import Sim


class GetFullSimStatusHandler:
    def __init__(self, sim_repository: ISimRepository):
        self.sim_repository = sim_repository

    def handle(self, query: GetFullSimStatusQuery) -> Sim:
        sim_id = UUID(str(query.sim_id))
        sim = self.sim_repository.find_full_by_id(sim_id)
        if not sim:
            raise SimNotFoundError(sim_id=sim_id)
        return sim
