from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_greet():
    assert client.get("/greet?name=Omar").json() == {"message": "Hello, Omar"}
