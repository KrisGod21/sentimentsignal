from pydantic import BaseModel
from typing import List

class SentimentRequest(BaseModel):
    stock: str
    headlines: List[str]
