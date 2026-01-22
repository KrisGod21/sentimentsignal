def get_signal(sentiment_score: int):
    if sentiment_score >= 70:
        return {
            "signal": "BUY",
            "message": "Strong positive sentiment suggests potential upside."
        }
    elif sentiment_score >= 40:
        return {
            "signal": "HOLD",
            "message": "Market sentiment is mixed. Wait for confirmation."
        }
    else:
        return {
            "signal": "SELL",
            "message": "Negative sentiment indicates potential downside."
        }
