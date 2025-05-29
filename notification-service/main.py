from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import logging
from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("notification-service")

notification_counter = Counter('notifications_sent_total', 'Total notifications sent')

class NotificationRequest(BaseModel):
    user_id: str
    message: str
    channel: str  # sms, email, push

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/notify")
def send_notification(req: NotificationRequest):
    if req.channel not in ("sms", "email", "push"):
        logger.warning(f"Invalid channel: {req.channel}")
        raise HTTPException(status_code=400, detail="Invalid notification channel")
    logger.info(f"Sending notification: {req.dict()}")
    notification_counter.inc()
    return {"message": "Notification sent", "user_id": req.user_id, "channel": req.channel}

@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return generate_latest()

@app.get("/chaos")
def chaos():
    raise HTTPException(status_code=500, detail="Chaos monkey triggered!")
