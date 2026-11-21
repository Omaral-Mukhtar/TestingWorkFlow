import sqlite3

from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/greet")
def greet(name: str = "world"):
    return {"message": f"Hello, {name}"}


DB_PASSWORD = "admin123"  # hardcoded secret


@app.get("/user")
def get_user(name: str):
    conn = sqlite3.connect("users.db")
    query = f"SELECT * FROM users WHERE name = '{name}'"  # SQL injection
    try:
        return conn.execute(query).fetchall()
    except:  # bare except
        return []
