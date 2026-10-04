from app.core.config import PROJECT_NAME, VERSION

def test_project_name() -> None:
    assert PROJECT_NAME == "SentinelAi"

def test_project_version() -> None:
    assert VERSION == "0.1.0"