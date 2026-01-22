# app/model.py
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

_analyzer = SentimentIntensityAnalyzer()

def analyze_headlines(headlines):
    """
    Input: list[str]
    Output: list of dicts: {label: 'POSITIVE'|'NEGATIVE'|'NEUTRAL', score: 0.0-1.0}
    """
    results = []
    for text in headlines:
        s = _analyzer.polarity_scores(text)
        compound = s["compound"]  # -1.0 .. 1.0
        if compound >= 0.05:
            label = "POSITIVE"
        elif compound <= -0.05:
            label = "NEGATIVE"
        else:
            label = "NEUTRAL"
        # Map compound (-1..1) to 0..1 for a "score" the UI can use
        score = round((compound + 1) / 2, 3)
        results.append({"label": label, "score": score, "raw": s})
    return results
