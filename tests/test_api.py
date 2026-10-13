from fastapi.testclient import TestClient

from app.api import routes
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "ok",
        "service": "SentinelAI",
    }


def test_ask_endpoint(monkeypatch):
    monkeypatch.setattr(
        routes,
        "get_services",
        lambda: (None, None, None),
    )

    monkeypatch.setattr(
        routes,
        "answer_question",
        lambda **kwargs: {
            "answer": "Report phishing emails immediately.",
            "sources": [
                {"source": "security_policy.pdf", "page": 1}
            ],
        },
    )

    response = client.post(
        "/ask",
        json={
            "question": "What should I do with a phishing email?"
        },
    )

    assert response.status_code == 200

    data = response.json()
    assert data["answer"] == "Report phishing emails immediately."
    assert data["sources"][0]["source"] == "security_policy.pdf"
    assert data["sources"][0]["page"] == 1


def test_ask_endpoint_rejects_empty_question():
    response = client.post("/ask", json={"question": ""})

    assert response.status_code == 422

def test_ask_endpoint_rejects_whitespace_question():
    response = client.post(
        "/ask",
        json={"question": "   "},
    )

    assert response.status_code == 422