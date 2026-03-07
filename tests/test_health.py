from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_ok() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"ok": True}


def test_docs_available() -> None:
    response = client.get("/docs")
    assert response.status_code == 200


def test_create_job_stub() -> None:
    response = client.post(
        "/jobs",
        json={"task_type": "example", "payload": {"message": "hello"}},
    )
    assert response.status_code == 201
    assert response.json() == {"job_id": "stub-job-1", "status": "queued"}
