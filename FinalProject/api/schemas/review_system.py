from pydantic import BaseModel

class ReviewSystem(BaseModel):
    message: str
    score: int
