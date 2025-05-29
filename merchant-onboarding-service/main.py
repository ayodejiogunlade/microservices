from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import logging
from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("merchant-onboarding-service")

merchant_counter = Counter('merchants_onboarded_total', 'Total merchants onboarded')

class MerchantOnboardRequest(BaseModel):
    merchant_name: str
    kyc_passed: bool

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/onboard")
def onboard_merchant(req: MerchantOnboardRequest):
    if not req.kyc_passed:
        logger.warning(f"KYC failed for merchant: {req.merchant_name}")
        raise HTTPException(status_code=400, detail="KYC not passed")
    logger.info(f"Onboarding merchant: {req.merchant_name}")
    merchant_counter.inc()
    return {"message": "Merchant onboarded", "merchant_name": req.merchant_name}

@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return generate_latest()

@app.get("/chaos")
def chaos():
    raise HTTPException(status_code=500, detail="Chaos monkey triggered!")
