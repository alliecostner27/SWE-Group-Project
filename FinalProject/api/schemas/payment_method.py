from pydantic import BaseModel, Field
from typing import Literal

class PaymentMethodBase(BaseModel):
    card_num: str = Field(..., description="credit/debit card number")
    transaction_status: Literal['pending', 'approved', 'failed']
    transaction_type: Literal['debit', 'credit']



class PaymentMethodCreate(PaymentMethodBase):
    pass

class PaymentMethodUpdate(PaymentMethodBase):
    pass

class PaymentMethod(PaymentMethodBase):
    id: int ## Primary Key
    
    class Config:
        from_attributes = True
