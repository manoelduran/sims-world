from ..impl.run_sim_decision_cycle import RunSimDecisionCycleCommand
from ...ports.i_sim_repository import ISimRepository
from ...ports.i_llm_service import ILLMService
from ...agents.memory_graph import SimMemoryGraph, SimAgentState
from ...exceptions.application_exceptions import SimNotFoundError


class RunSimDecisionCycleHandler:
    def __init__(self, sim_repository: ISimRepository, llm_service: ILLMService):
        self.repo = sim_repository
        self.llm = llm_service

        # Construir e compilar o grafo UMA VEZ
        graph_builder = SimMemoryGraph(self.repo, self.llm)
        self.graph_app = graph_builder.build_graph()

    def handle(self, command: RunSimDecisionCycleCommand) -> SimAgentState:
        # 1. Buscar o Sim (necessário para o prompt de personalidade)
        sim = self.repo.find_full_by_id(command.sim_id)
        if not sim:
            raise SimNotFoundError(sim_id=command.sim_id)

        # 2. Definir o estado inicial
        initial_state = SimAgentState(
            sim=sim,
            perception=command.perception,
            stm_log=[],
            retrieved_memories=[],
            reflection="",
            importance_score=0,
            action="",
            feeling="",
        )

        # 3. Invocar o grafo
        final_state_data = self.graph_app.invoke(initial_state)

        # Map the dict result to a SimAgentState instance so the handler returns the expected type
        final_state = SimAgentState(
            sim=initial_state["sim"],
            perception=initial_state["perception"],
            stm_log=final_state_data.get("stm_log", initial_state["stm_log"]),
            retrieved_memories=final_state_data.get(
                "retrieved_memories", initial_state["retrieved_memories"]
            ),
            reflection=final_state_data.get("reflection", ""),
            importance_score=final_state_data.get("importance_score", 0),
            action=final_state_data.get("action", ""),
            feeling=final_state_data.get("feeling", ""),
        )

        self.repo.update_sim_status(
            sim_id=sim.id,
            feeling=final_state["feeling"],
            action=final_state["action"],
        )
        self.repo.save_action_to_log(
            sim_id=sim.id,
            action_type="reflection",
            description=final_state["reflection"],
        )
        self.repo.save_action_to_log(
            sim_id=sim.id, action_type="action", description=final_state["action"]
        )

        return final_state
