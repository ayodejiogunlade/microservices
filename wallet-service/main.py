from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import logging
from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("wallet-service")

wallet_counter = Counter('wallet_transactions_total', 'Total wallet transactions')

class WalletTransactionRequest(BaseModel):
    user_id: str
    amount: float
    type: str  # deposit or withdraw

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/wallets/transaction")
def wallet_transaction(tx: WalletTransactionRequest):
    if tx.amount <= 0 or tx.type not in ("deposit", "withdraw"):
        logger.warning(f"Invalid transaction: {tx.dict()}")
        raise HTTPException(status_code=400, detail="Invalid transaction request")
    logger.info(f"Processing wallet transaction: {tx.dict()}")
    wallet_counter.inc()
    return {"message": "Transaction complete", "user_id": tx.user_id, "amount": tx.amount, "type": tx.type}

@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return generate_latest()

@app.get("/chaos")
def chaos():
    raise HTTPException(status_code=500, detail="Chaos monkey triggered!")
