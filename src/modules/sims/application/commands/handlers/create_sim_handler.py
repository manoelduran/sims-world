from ....application.commands.impl.create_sim import CreateSimCommand
from ....application.ports.i_sim_repository import ISimRepository
from ....domain.entities.needs import SimNeeds
from ....domain.entities.status import SimStatus
from ....domain.entities.sim import Sim


class CreateSimHandler:
    def __init__(self, sim_repository: ISimRepository):
        self.sim_repository = sim_repository

    def handle(self, command: CreateSimCommand) -> Sim:
        sim_to_create = Sim(
            name=command.name,
            personality_summary=command.personality,
            age_in_days=25,
            life_stage="adult",
            is_alive=True,
            needs=SimNeeds(hunger=100, energy=100, social=75, hygiene=100),
            status=SimStatus(current_feeling="normal"),
        )
        print("Creating SIM:", sim_to_create)
        return self.sim_repository.save(sim_to_create)
