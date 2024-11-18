from datetime import date
from pydantic import BaseModel

class ReviewSystem(BaseModel):
    message: str
    score: int
