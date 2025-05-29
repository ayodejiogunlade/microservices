from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import logging
from prometheus_client import Counter, generate_latest
from fastapi.responses import PlainTextResponse

app = FastAPI()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("analytics-service")

analytics_counter = Counter('analytics_reports_total', 'Total analytics reports generated')

class AnalyticsReportRequest(BaseModel):
    report_type: str
    start_date: str
    end_date: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/analytics/report")
def get_report(report_type: str = "summary", start_date: str = None, end_date: str = None):
    logger.info(f"Generating report: type={report_type}, start={start_date}, end={end_date}")
    analytics_counter.inc()
    # Simulate report data
    return {"report": {"type": report_type, "start": start_date, "end": end_date, "data": []}}

@app.get("/metrics", response_class=PlainTextResponse)
def metrics():
    return generate_latest()

@app.get("/chaos")
def chaos():
    raise HTTPException(status_code=500, detail="Chaos monkey triggered!")
