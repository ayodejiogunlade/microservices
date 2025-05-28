from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/onboard")
def onboard_merchant():
    # TODO: Implement merchant onboarding logic
    return {"message": "Merchant onboarded"}
