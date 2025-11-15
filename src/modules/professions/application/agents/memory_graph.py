from typing import TypedDict, List

from langgraph.graph import StateGraph, END

from src.modules.sims.domain.entities.sim import Sim
from src.modules.sims.application.ports.i_llm_service import ILLMService
from src.modules.sims.application.ports.i_sim_repository import ISimRepository


class SimAgentState(TypedDict):
    sim: Sim
    perception: str  # A nova informação (ex: "Bob disse oi")
    stm_log: List[str]  # Memória de Curto Prazo: log das últimas X percepções
    # RAG
    retrieved_memories: List[str]  # O que o RAG buscou da LTM (pgvector)
    # Sumarização / Reflexão
    reflection: str  # O "pensamento" do Sim após sumarizar tudo
    importance_score: int  # Quão importante foi esse pensamento (1-10)
    feeling: str
    action: str  # A ação final decidida (ex: "Dizer oi para Bob")


class SimMemoryGraph:
    def __init__(self, repo: ISimRepository, llm: ILLMService):
        self.repo = repo
        self.llm = llm

    # --- 3. Definir os Nós ---
    def retrieve_stm(self, state: SimAgentState):
        logs = self.repo.get_short_term_memory(state["sim"].id, k=5)
        # Inverter para ordem cronológica
        return {"stm_log": [log.description for log in reversed(logs)]}

    def retrieve_ltm_rag(self, state: SimAgentState):
        embedding = self.llm.generate_embedding(state["perception"])
        mems = self.repo.find_relevant_memories(state["sim"].id, embedding, k=3)
        return {"retrieved_memories": [mem.description for mem in mems]}

    def reflect_and_summarize(self, state: SimAgentState):
        prompt = f"""
            Você está AGINDO como {state["sim"].name}.
            Sua persona é: {state["sim"].personality_summary}.
            Você NÃO é um assistente de IA. Você é este personagem.
            Seu estado atual é: Fome={state["sim"].needs.hunger}, Energia={state["sim"].needs.energy}.

            **O Que Aconteceu:**
            Você acabou de perceber: "{state["perception"]}"

            **Memórias Recentes:**
            {chr(10).join(f"- {log}" for log in state["stm_log"])}

            **Memórias Relevantes do Passado:**
            {chr(10).join(f"- {mem}" for mem in state["retrieved_memories"])}

            **Sua Tarefa (Responda APENAS com JSON):**
            1.  **reflection**: Escreva seu pensamento interno em primeira pessoa, com a voz e emoções do seu personagem. NÃO analise o processo. APENAS sinta e pense.
            2.  **importance_score**: Avalie a importância desse pensamento em uma escala de 1 a 10.
            3.  **feeling**: Diga seu sentimento principal (ex: 'feliz', 'ansioso', 'curioso').
        """
        response_json = self.llm.invoke_json(prompt)
        return {
            "reflection": response_json.get("reflection"),
            "importance_score": response_json.get("importance_score"),
            "feeling": response_json.get("feeling"),
        }

    def decide_action(self, state: SimAgentState):
        prompt = f"""
        Você é {state["sim"].name}. Seu estado é: Fome={state["sim"].needs.hunger}, Energia={state["sim"].needs.energy}.
        Seu sentimento atual é: {state["feeling"]}.
        Seu último pensamento foi: "{state["reflection"]}"

        Qual é a sua próxima ação imediata? Seja breve, descreva a ação.
        Exemplos: "ir para a cozinha fazer um lanche", "cumprimentar Bob de volta", "ignorar Alice e ir dormir".
        """
        action = self.llm.invoke(prompt)
        return {"action": action.strip().strip('"')}

    def save_to_ltm(self, state: SimAgentState):
        embedding = self.llm.generate_embedding(state["reflection"])
        self.repo.add_memory(
            sim_id=state["sim"].id,
            description=state["reflection"],
            importance=state["importance_score"],
            embedding=embedding,
        )
        return {}  # Nenhum estado para atualizar

    # --- 4. Definir as Bordas Condicionais ---
    def should_save_to_ltm(self, state: SimAgentState):
        if state["importance_score"] >= 7:
            return "save_to_ltm"
        else:
            return END

    # --- 5. Construir o Grafo ---
    def build_graph(self):
        workflow = StateGraph(SimAgentState)

        workflow.add_node("retrieve_stm", self.retrieve_stm)
        workflow.add_node("retrieve_ltm_rag", self.retrieve_ltm_rag)
        workflow.add_node("reflect_and_summarize", self.reflect_and_summarize)
        workflow.add_node("decide_action", self.decide_action)
        workflow.add_node("save_to_ltm", self.save_to_ltm)

        workflow.set_entry_point("retrieve_stm")
        workflow.add_edge("retrieve_stm", "retrieve_ltm_rag")
        workflow.add_edge("retrieve_ltm_rag", "reflect_and_summarize")
        workflow.add_edge("reflect_and_summarize", "decide_action")

        workflow.add_conditional_edges(
            "decide_action",
            self.should_save_to_ltm,
        )
        workflow.add_edge("save_to_ltm", END)

        return workflow.compile()
