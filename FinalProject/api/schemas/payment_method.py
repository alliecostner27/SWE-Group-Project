from pydantic import BaseModel, Field
from typing import Literal

class PaymentMethodBase(BaseModel):
    card_num: str = Field(..., description="credit/debit card number")
    transaction_status: Literal['pending', 'approved', 'failed'] = Field(..., description="transaction status")
    transaction_type: Literal['debit', 'credit'] = Field(..., description="transaction type")


class PaymentMethodCreate(PaymentMethodBase):
    pass

class PaymentMethodUpdate(PaymentMethodBase):
    pass

class PaymentMethod(PaymentMethodBase):
    id: int ## Primary Key
    
    class ConfigDicta:
        orm_mode = True
