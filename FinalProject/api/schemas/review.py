from pydantic import BaseModel

class ReviewSystemBase(BaseModel):
    message: str
    score: int
    
    
class Review(ReviewSystemBase):
    id: int
    
    class Config:
        orm_mode = True
