from fastapi import FastAPI
from app.schemas import SentimentRequest
from app.model import analyze_headlines

app = FastAPI(title="SentimentSignal API")

@app.get("/")
def health():
    return {"status": "API running"}

@app.post("/analyze")
def analyze(req: SentimentRequest):
    results = analyze_headlines(req.headlines)

    pos = sum(1 for r in results if r["label"] == "POSITIVE")
    neg = sum(1 for r in results if r["label"] == "NEGATIVE")

    if pos > neg:
        signal = "BUY"
    elif neg > pos:
        signal = "SELL"
    else:
        signal = "HOLD"

    return {
        "stock": req.stock,
        "signal": signal,
        "sentiment_breakdown": results
    }
