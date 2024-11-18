from pydantic import BaseModel

class CustomerBase(BaseModel):
    name: str
    email: str
    phoneNum: str
    address: str
    
    
class Customer(CustomerBase):
    id: int
    
    class Config:
        orm_mode = True
        
        