from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DateTime
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class PaymentMethod(Base):
    __tablename__ = "PaymentMethods"

    id = Column(Integer, primary_key=True, autoincrement=True) 
    cardNum = Column(Integer, nullable=False) 
    transactionStatus = Column(String(50), nullable=False)
    transactionType = Column(String(50), nullable=False)
