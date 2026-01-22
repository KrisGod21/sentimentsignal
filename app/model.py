from transformers import pipeline

_sentiment_model = None

def get_model():
    global _sentiment_model
    if _sentiment_model is None:
        _sentiment_model = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            device=-1  # force CPU
        )
    return _sentiment_model


def analyze_sentiment(texts: list[str]):
    model = get_model()
    results = model(texts)

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
    sentiment_score = int(((score_sum / total) + 1) * 50)

    return {
        "sentiment_score": sentiment_score,
        "positive": int((pos / total) * 100),
        "neutral": int((neu / total) * 100),
        "negative": int((neg / total) * 100),
    }
