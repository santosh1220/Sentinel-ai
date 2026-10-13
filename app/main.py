from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(
    title="SentinelAI API",
    description="Enterprise knowledge assistant powered by RAG and a local LLM.",
    version="0.1.0",
)

app.include_router(router)