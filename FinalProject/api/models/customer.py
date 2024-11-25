from sqlalchemy import Column, Integer, String
from ..dependencies.database import Base


class Customer(Base):
    __tablename__ = "customers"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), index=True, nullable=False)  
    email = Column(String(255), index=True, nullable=False)  
    phone_num = Column(String(20), index=True, nullable=False)
    address = Column(String(300), index=True, nullable=False) 
