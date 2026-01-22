from transformers import pipeline

# LOAD MODEL ONCE (CRITICAL)
sentiment_pipeline = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    device=-1  # CPU only
)

def analyze_headlines(headlines):
    return sentiment_pipeline(headlines)
