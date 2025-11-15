from ...ports.i_sim_repository import ISimRepository
from ....domain.entities.sim import Sim
from ..impl.set_sim_profession import SetSimProfessionCommand
from ...exceptions.application_exceptions import SimNotFoundError


class SetSimProfessionHandler:
    def __init__(self, sim_repository: ISimRepository):
        self.sim_repository = sim_repository

    def handle(self, command: SetSimProfessionCommand) -> Sim:
        updated_sim = self.sim_repository.set_profession(
            command.sim_id, command.profession_id
        )
        if not updated_sim:
            raise SimNotFoundError(sim_id=command.sim_id)

        return updated_sim
