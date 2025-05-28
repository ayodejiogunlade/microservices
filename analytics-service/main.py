from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/analytics/report")
def get_report():
    # TODO: Implement analytics report logic
    return {"report": {}}
