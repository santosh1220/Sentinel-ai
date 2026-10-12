from app.llm.client import LLMClient
from app.rag.embeddings import EmbeddingService
from app.rag.qa import answer_question
from app.rag.vector_store import VectorStore


def main() -> None:
    embedding_service = EmbeddingService()
    vector_store = VectorStore()
    llm_client = LLMClient()

    question = "What should I do if I receive a phishing email?"

    result = answer_question(
        question=question,
        embedding_service=embedding_service,
        vector_store=vector_store,
        llm_client=llm_client,
        top_k=3,
    )

    print("\nQuestion:")
    print(question)

    print("\nSentinelAI Answer:")
    print(result["answer"])

    print("\nRetrieved Sources:")
    for source in result["sources"]:
        print(
            f"- {source.get('source', 'Unknown source')}, "
            f"page {source.get('page', 'Unknown page')}"
        )


if __name__ == "__main__":
    main()