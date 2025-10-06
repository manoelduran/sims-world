from fastapi import FastAPI
from src.modules.sims.presentation.api import sim_router

app = FastAPI(
    title="Sims World API",
    description="Uma API para simular a vida de agentes autônomos com LangGraph e Gemini.",
    version="0.1.0",
)


@app.get("/health", tags=["Health"])
def health_check():
    """Verifica se a API está funcionando."""
    return {"status": "ok", "message": "API is running!"}


app.include_router(sim_router.router, prefix="/api/v1", tags=["Sims"])
