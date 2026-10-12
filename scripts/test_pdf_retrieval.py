from app.rag.embeddings import EmbeddingService
from app.rag.vector_store import VectorStore


def main() -> None:
    embedding_service = EmbeddingService()
    vector_store = VectorStore()

    query = "What should I do if I receive a phishing email?"

    query_embedding = embedding_service.embed_text(query)

    results = vector_store.search(
        query_embedding.tolist(),
        top_k=3,
    )

    print(f"\nQuery: {query}")

    for document, metadata in zip(
        results["documents"][0],
        results["metadatas"][0],
    ):
        print(f"\nDocument: {document}")
        print(f"Source: {metadata['source']}")
        print(f"Page: {metadata['page']}")

        assert metadata["source"] == "security_policy.pdf"
        assert metadata["page"] in (1, 2)


if __name__ == "__main__":
    main()