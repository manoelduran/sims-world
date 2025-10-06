from modules.sims.application.commands.impl.create_sim import CreateSimCommand
from modules.sims.application.ports.i_sim_repository import ISimRepository
from ....domain.entities.sim import Sim


class CreateSimHandler:
    def __init__(self, sim_repository: ISimRepository):
        self.sim_repository = sim_repository

    def handle(self, command: CreateSimCommand) -> Sim:
        new_sim = Sim(name=command.name, personality=command.personality)

        return self.sim_repository.save(new_sim)