from app.rag.retriever import retrieve


query = "What should I do if I receive a phishing email?"

results = retrieve(query, top_k=3)

print(f"\nQuery: {query}\n")

for rank, (document, score) in enumerate(results, start=1):
    print(f"{rank}. Score: {score:.4f}")
    print(f"   {document}\n")