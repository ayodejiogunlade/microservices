from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/wallets/transaction")
def wallet_transaction():
    # TODO: Implement wallet transaction logic
    return {"message": "Transaction complete"}
