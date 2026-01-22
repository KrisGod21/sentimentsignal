from fastapi import FastAPI
from app.schemas import SentimentRequest
from app.model import analyze_headlines

app = FastAPI(title="SentimentSignal API")

@app.get("/")
def root():
    return {"status": "API running"}

@app.post("/analyze")
def analyze(req: SentimentRequest):
    results = analyze_headlines(req.headlines)

    pos = sum(1 for r in results if r["label"] == "POSITIVE")
    neg = sum(1 for r in results if r["label"] == "NEGATIVE")

    signal = "BUY" if pos > neg else "SELL" if neg > pos else "HOLD"

    return {
        "stock": req.stock,
        "signal": signal,
        "results": results
    }
