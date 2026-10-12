import pytest

from app.rag.context_builder import build_context

def test_build_context_includes_sources_and_pages():
    documents = [
        "Report phishing emails immediately.",
        "Security incidents must be reported within 30 minutes.",
    ]

    metadatas = [
        {"source": "security_policy.pdf", "page": 1},
        {"source": "security_policy.pdf", "page": 2},
    ]

    context = build_context(documents, metadatas)

    assert "Report phishing emails immediately." in context
    assert "security_policy.pdf, page 1" in context
    assert "security_policy.pdf, page 2" in context


def test_build_context_rejects_mismatched_metadata():
    with pytest.raises(ValueError):
        build_context(
            ["One document", "Another document"],
            [{"source": "policy.pdf", "page": 1}],
        )
