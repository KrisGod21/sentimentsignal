from pydantic import BaseModel
from typing import List

class SentimentRequest(BaseModel):
    stock: str
    headlines: List[str]

class SentimentResponse(BaseModel):
    stock: str
    price: float
    change: float
    sentiment_score: int
    signal: str
    signal_message: str
    distribution: dict
