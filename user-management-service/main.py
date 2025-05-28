from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/users")
def create_user():
    # TODO: Implement user creation logic
    return {"message": "User created"}
