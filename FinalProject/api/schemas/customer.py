from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    name: str
    email: str
    phone_num: str
    address: str
    
    
class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    pass


class Customer(CustomerBase):
    id: int ## Primary key
    
    class ConfigDict:
        from_attributes = True
        
        
        