def build_context(
    documents: list[str],
    metadatas: list[dict | None],
) -> str:
    if len(documents) != len(metadatas):
        raise ValueError(
            "Each document must have matching metadata."
        )

    context_parts = []

    for index, (document, metadata) in enumerate(
        zip(documents, metadatas),
        start=1,
    ):
        metadata = metadata or {}

        source = metadata.get("source", "Unknown source")
        page = metadata.get("page", "Unknown page")

        context_parts.append(
            f"[Source {index}: {source}, page {page}]\n"
            f"{document}"
        )

    return "\n\n".join(context_parts)