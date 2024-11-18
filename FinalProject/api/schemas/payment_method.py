from pydantic import BaseModel

class PaymentMethod(BaseModel):
    cardNum: int
    transactionStatus: str
    transactionType: str
