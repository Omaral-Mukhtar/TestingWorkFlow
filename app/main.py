from fastapi import FastAPI

app = FastAPI()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/greet")
def greet(name: str = "world"):
    return {"message": f"Hello, {name}"}
