import chromadb


class VectorStore:
    def __init__(self, collection_name: str = "sentinel_documents"):
        self.client = chromadb.PersistentClient(
            path="data/chroma"
        )

        self.collection = self.client.get_or_create_collection(
            name=collection_name
        )

    def add_documents(
        self,
        documents: list[str],
        embeddings: list[list[float]],
        metadatas: list[dict],
    ) -> None:

        ids = [
            f"doc_{index}"
            for index in range(len(documents))
        ]

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas
        )

    def search(
        self,
        query_embedding: list[float],
        top_k: int = 3,
    ):
        return self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k,
        )