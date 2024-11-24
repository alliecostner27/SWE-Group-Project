from pydantic import BaseModel

class PaymentMethodBase(BaseModel):
    cardNum: int
    transactionStatus: str
    transactionType: str
    

class PaymentMethod(PaymentMethodBase):
    id: int
    
    class ConfigDict:
        orm_mode = True
