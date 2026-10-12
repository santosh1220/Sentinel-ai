from app.llm.client import LLMClient
from app.rag.embeddings import EmbeddingService
from app.rag.pipeline import build_retrieval_context
from app.rag.vector_store import VectorStore


def answer_question(
    question: str,
    embedding_service: EmbeddingService,
    vector_store: VectorStore,
    llm_client: LLMClient,
    top_k: int = 3,
) -> dict:
    if not question.strip():
        raise ValueError("Question cannot be empty.")

    context, sources = build_retrieval_context(
        query=question,
        embedding_service=embedding_service,
        vector_store=vector_store,
        top_k=top_k,
    )

    if not context:
        return {
            "answer": (
                "I couldn't find sufficient evidence in the "
                "available documents to answer this question."
            ),
            "sources": [],
        }

    answer = llm_client.generate_answer(
        question=question,
        context=context,
    )

    return {
        "answer": answer,
        "sources": sources,
    }