from pydantic import BaseModel

class PaymentMethodBase(BaseModel):
    cardNum: int
    transactionStatus: str
    transactionType: str
    

class PaymentMethod(PaymentMethodBase):
    id: int
    
    class Config:
        orm_mode = True
