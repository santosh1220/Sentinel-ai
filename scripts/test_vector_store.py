from app.rag.embeddings import EmbeddingService
from app.rag.vector_store import VectorStore


documents = [
    "Employees must report phishing emails to the security team immediately.",
    "Employees should use multi-factor authentication when accessing company systems.",
    "Passwords must be at least 12 characters long.",
    "Security incidents must be reported to the SOC within 30 minutes.",
    "Employees should lock their computer when leaving their desk.",
]


embedding_service = EmbeddingService()

embeddings = embedding_service.embed_documents(documents)

vector_store = VectorStore()

vector_store.add_documents(
    documents,
    embeddings.tolist(),
)

query = "How quickly must security incidents be reported?"

query_embedding = embedding_service.embed_text(query)

results = vector_store.search(
    query_embedding.tolist(),
    top_k=3,
)

print("\nQuery:")
print(query)

print("\nRetrieved documents:")

for document in results["documents"][0]:
    print("-", document)