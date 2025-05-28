from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/notify")
def send_notification():
    # TODO: Implement notification logic
    return {"message": "Notification sent"}
