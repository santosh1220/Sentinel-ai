from app.rag.embeddings import EmbeddingService
from app.rag.pipeline import build_retrieval_context
from app.rag.vector_store import VectorStore


def main() -> None:
    embedding_service = EmbeddingService()
    vector_store = VectorStore()

    query = "What should I do if I receive a phishing email?"

    context, sources = build_retrieval_context(
        query=query,
        embedding_service=embedding_service,
        vector_store=vector_store,
        top_k=3,
    )

    print(f"\nQuestion: {query}")
    print("\nPrepared context:")
    print(context)

    print("\nSources:")
    for source in sources:
        print(
            f"- {source.get('source', 'Unknown source')}, "
            f"page {source.get('page', 'Unknown page')}"
        )


if __name__ == "__main__":
    main()