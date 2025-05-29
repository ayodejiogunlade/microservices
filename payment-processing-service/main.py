from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import logging
from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("payment-processing-service")

# Prometheus metrics
payment_counter = Counter('payments_processed_total', 'Total payments processed')

class PaymentRequest(BaseModel):
    amount: float
    currency: str
    user_id: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/payments")
def process_payment(payment: PaymentRequest):
    if payment.amount <= 0:
        logger.warning(f"Invalid payment amount: {payment.amount}")
        raise HTTPException(status_code=400, detail="Amount must be positive")
    # Simulate payment processing logic
    logger.info(f"Processing payment: {payment.dict()}")
    payment_counter.inc()
    return {"message": "Payment processed", "amount": payment.amount, "currency": payment.currency, "user_id": payment.user_id}

@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return generate_latest()

@app.get("/fraud-check")
def fraud_check(user_id: str):
    # Stub for ML fraud detection
    return {"user_id": user_id, "fraudulent": False}

@app.get("/chaos")
def chaos():
    # Stub for chaos engineering
    raise HTTPException(status_code=500, detail="Chaos monkey triggered!")
