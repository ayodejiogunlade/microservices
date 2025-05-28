from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/payments")
def process_payment():
    # TODO: Implement payment processing logic
    return {"message": "Payment processed"}
