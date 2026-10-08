from app.rag.embeddings import EmbeddingService

def test_embed_text():
    service = EmbeddingService()

    vector = service.embed_text(
        "How do I report a phishing email?"
    )

    assert len(vector) == 384