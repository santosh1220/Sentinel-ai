from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DOCUMENTS = [
    "Employees must report phishing emails to the security team immediately.",
    "Employees should use multi-factor authentication when accessing company systems.",
    "Passwords must be at least 12 characters long.",
    "Security incidents must be reported to the SOC within 30 minutes.",
    "Employees should lock their computer when leaving their desk.",
]


def retrieve(query: str, top_k: int = 3) -> list[tuple[str, float]]:
    vectorizer = TfidfVectorizer()

    document_vectors = vectorizer.fit_transform(DOCUMENTS)
    query_vector = vectorizer.transform([query])

    similarities = cosine_similarity(
        query_vector,
        document_vectors,
    )[0]

    ranked_indexes = similarities.argsort()[::-1][:top_k]

    results = [
        (DOCUMENTS[index], similarities[index])
        for index in ranked_indexes
    ]

    return results