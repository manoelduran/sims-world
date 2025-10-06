from uuid import UUID

class SimNotFoundError(Exception):
    def __init__(self, sim_id: UUID):
        self.sim_id = sim_id
        super().__init__(f"Sim com ID {sim_id} não encontrado.")