from pydantic import BaseModel
from datetime import date
from typing import Optional

class PromoBase(BaseModel):
    code: int
    expirationDate: date
    

class PromoCreate(PromoBase):
    pass


class Promo(PromoBase):
    id: int
    
    class Config:
        orm_mode = True
        



