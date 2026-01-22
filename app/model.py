from transformers import pipeline

sentiment_model = pipeline("sentiment-analysis")

def analyze_sentiment(texts: list[str]):
    results = sentiment_model(texts)

    pos = neg = neu = 0
    score_sum = 0

    for r in results:
        if r["label"] == "POSITIVE":
            pos += 1
            score_sum += r["score"]
        elif r["label"] == "NEGATIVE":
            neg += 1
            score_sum -= r["score"]
        else:
            neu += 1

    total = len(results)
    sentiment_score = int(((score_sum / total) + 1) * 50)  # 0–100 scale

    return {
        "sentiment_score": sentiment_score,
        "positive": int((pos / total) * 100),
        "neutral": int((neu / total) * 100),
        "negative": int((neg / total) * 100),
    }
