import sqlite3

from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_greet():
    assert client.get("/greet?name=Omar").json() == {"message": "Hello, Omar"}


def test_user(tmp_path, monkeypatch):
    db = tmp_path / "t.db"
    conn = sqlite3.connect(db)
    conn.execute("CREATE TABLE users (name TEXT)")
    conn.execute("INSERT INTO users VALUES ('Omar')")
    conn.commit()
    conn.close()

    monkeypatch.setenv("DB_PATH", str(db))
    assert client.get("/user?name=Omar").json() == [["Omar"]]
