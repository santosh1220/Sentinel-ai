from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


documents = [
    "Employees must report phishing emails to the security team immediately.",
    "Employees should use multi-factor authentication when accessing company systems.",
    "Passwords must be at least 12 characters long.",
    "Security incidents must be reported to the SOC within 30 minutes.",
    "Employees should lock their computer when leaving their desk.",
]


query = "how can i report a suspicious email?"


model = SentenceTransformer("all-MiniLM-L6-v2")

document_embeddings = model.encode(documents)
query_embedding = model.encode([query])

similarities = cosine_similarity(
    query_embedding,
    document_embeddings,
)[0]

ranked_indexes = similarities.argsort()[::-1]

print(f"\nQuery: {query}\n")

for rank, index in enumerate(ranked_indexes, start=1):
    print(f"{rank}. Score: {similarities[index]:.4f}")
    print(f"   {documents[index]}\n")