from app.rag.context_builder import build_context
from app.rag.embeddings import EmbeddingService
from app.rag.vector_store import VectorStore


def build_retrieval_context(
    query: str,
    embedding_service: EmbeddingService,
    vector_store: VectorStore,
    top_k: int = 3,
) -> tuple[str, list[dict]]:
    if not query.strip():
        raise ValueError("Query cannot be empty.")

    query_embedding = embedding_service.embed_text(query)

    results = vector_store.search(
        query_embedding.tolist(),
        top_k=top_k,
    )

    documents = results["documents"][0] or []
    metadatas = results["metadatas"][0] or []

    if not documents:
        return "", []

    sources = [
        metadata or {}
        for metadata in metadatas
    ]

    context = build_context(documents, sources)

    return context, sources