from app.rag.chunking import chunk_text

def test_chunk_text():
    text = " ".join(f"word{i}" for i in range(1, 251))  # Create a long text with 251 words

    chunks = chunk_text(text, chunk_size=100, overlap=20)

    assert len(chunks) == 3  # Expecting 3 chunks
    assert chunks[0].split()[0] == "word1"  # First chunk starts with word1
    assert chunks[1].split()[0] == "word81"  # Second chunk starts with word81
    assert chunks[2].split()[0] == "word161"  # Third chunk starts with word161