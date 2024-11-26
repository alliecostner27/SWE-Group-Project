from pydantic import BaseModel
from typing import Optional

class CustomerBase(BaseModel):
    id: int
    name: str
    email: str
    phone_num: str
    address: str
    
    
class CustomerCreate(CustomerBase):
    pass


class CustomerUpdate(CustomerBase):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    phone_num: Optional[str] = None
    address: Optional[str] = None


class Customer(CustomerBase):
    id: int ## Primary key
    
    class ConfigDict:
        from_attributes = True
        
        
        