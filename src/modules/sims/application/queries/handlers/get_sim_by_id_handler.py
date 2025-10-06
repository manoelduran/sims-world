from modules.sims.application.exceptions.application_exceptions import SimNotFoundError
from modules.sims.application.ports.i_sim_repository import ISimRepository
from modules.sims.application.queries.impl.get_sim_by_id import GetSimByIdQuery
from modules.sims.domain.entities.sim import Sim


class GetSimByIdHandler:
    def __init__(self, sim_repository: ISimRepository):
        self.sim_repository = sim_repository

    def handle(self, query: GetSimByIdQuery) -> Sim:
        sim = self.sim_repository.find_by_id(query.sim_id)

        if not sim:
            raise SimNotFoundError(sim_id=query.sim_id)

        return sim
