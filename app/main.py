import os
import sqlite3

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/greet")
def greet(name: str = "world"):
    return {"message": f"Hello, {name}"}


@app.get("/user")
def get_user(name: str):
    conn = sqlite3.connect(os.environ.get("DB_PATH", "users.db"))
    try:
        return conn.execute("SELECT * FROM users WHERE name = ?", (name,)).fetchall()
    except sqlite3.Error:
        return []
    finally:
        conn.close()
