from fastapi import FastAPI
from app.schemas import SentimentRequest
from app.model import analyze_sentiment
from app.utils import get_signal

app = FastAPI(title="SentimentSignal API")


@app.post("/analyze")
def analyze(request: SentimentRequest):
    sentiment = analyze_sentiment(request.headlines)
    signal_data = get_signal(sentiment["sentiment_score"])

    return {
        "stock": request.stock,
        "price": 2847.55,
        "change": 1.62,
        "sentiment_score": sentiment["sentiment_score"],
        "signal": signal_data["signal"],
        "signal_message": signal_data["message"],
        "distribution": {
            "positive": sentiment["positive"],
            "neutral": sentiment["neutral"],
            "negative": sentiment["negative"]
        }
    }
