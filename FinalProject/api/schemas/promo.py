from pydantic import BaseModel, Field
from datetime import date

class PromoBase(BaseModel):
    code: str = Field(..., description="Promo Code")
    expirationDate: date = Field(..., description="Expiration Date for Promo Code")
    

class PromoCreate(PromoBase):
    pass

class PromoUpdate(PromoBase):
    pass

class Promo(PromoBase):
    id: int ##Primary Key
    
    class ConfigDict:
        from_attributes = True
        



