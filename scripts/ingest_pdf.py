from app.rag.chunking import chunk_text
from app.rag.embeddings import EmbeddingService
from app.rag.ingestion import extract_pdf_pages
from app.rag.vector_store import VectorStore


PDF_PATH = "data/security_policy.pdf"


def main() -> None:
    pages = extract_pdf_pages(PDF_PATH)

    documents = []
    metadatas = []

    for page in pages:
        chunks = chunk_text(
            page["text"],
            chunk_size=100,
            overlap=20,
        )

        for chunk in chunks:
            documents.append(chunk)
            metadatas.append(page["metadata"])

    if not documents:
        print("No text found in the PDF.")
        return

    embedding_service = EmbeddingService()

    embeddings = embedding_service.embed_documents(
        documents
    )

    vector_store = VectorStore()

    vector_store.add_documents(
        documents,
        embeddings.tolist(),
        metadatas,
    )

    print(f"PDF: {PDF_PATH}")
    print(f"Pages processed: {len(pages)}")
    print(f"Chunks indexed: {len(documents)}")


if __name__ == "__main__":
    main()
