from fastapi import APIRouter, HTTPException

from app.api.schemas import (
    AskRequest,
    AskResponse,
    HealthResponse,
    SourceResponse,
)
from app.llm.client import LLMClient
from app.rag.embeddings import EmbeddingService
from app.rag.qa import answer_question
from app.rag.vector_store import VectorStore

router = APIRouter()

# Reuse these services across requests.
embedding_service = None
vector_store = None
llm_client = None


def get_services():
    global embedding_service, vector_store, llm_client

    if embedding_service is None:
        embedding_service = EmbeddingService()
        vector_store = VectorStore()
        llm_client = LLMClient()

    return embedding_service, vector_store, llm_client


@router.get("/health", response_model=HealthResponse)
def health_check():
    return {
        "status": "ok",
        "service": "SentinelAI",
    }


@router.post("/ask", response_model=AskResponse)
def ask_question(request: AskRequest):
    if not request.question.strip():
        raise HTTPException(
            status_code=422,
            detail="Question cannot be empty.",
        )

    try:
        embeddings, store, llm = get_services()

        result = answer_question(
            question=request.question,
            embedding_service=embeddings,
            vector_store=store,
            llm_client=llm,
            top_k=3,
        )

        return {
            "answer": result["answer"],
            "sources": [
                SourceResponse(
                    source=source.get("source", "Unknown source"),
                    page=source.get("page", "Unknown page"),
                )
                for source in result["sources"]
            ],
        }

    except ValueError as exc:
        raise HTTPException(
            status_code=422,
            detail=str(exc),
        ) from exc
    except Exception as exc:
        raise HTTPException(
            status_code=503,
            detail="SentinelAI could not process the question. "
            "Check that Ollama is running and the model is available.",
        ) from exc