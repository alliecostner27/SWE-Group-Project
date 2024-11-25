from pydantic import BaseModel, Field
from .orders import Order


class ReviewBase(BaseModel):
    order_id: int ## reference associated order id
    review: str = Field(..., description='The review text')
    score: int = Field(..., ge=1, le=5,  description='The score of the review (1 to 5)')


class ReviewCreate(ReviewBase):
    pass


class Review(ReviewBase):
    id: int ## Primary Key
    
    class Config:
        from_attributes = True
