from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import logging
from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("user-management-service")

# Prometheus metrics
user_counter = Counter('users_created_total', 'Total users created')

class UserRequest(BaseModel):
    username: str
    email: str
    password: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/users")
def create_user(user: UserRequest):
    if not user.username or not user.email or not user.password:
        logger.warning("Missing user fields")
        raise HTTPException(status_code=400, detail="All fields required")
    logger.info(f"Creating user: {user.dict(exclude={'password'})}")
    user_counter.inc()
    return {"message": "User created", "username": user.username, "email": user.email}

@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return generate_latest()

@app.get("/chaos")
def chaos():
    raise HTTPException(status_code=500, detail="Chaos monkey triggered!")
