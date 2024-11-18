from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class PaymentMethod(Base):
    __tablename__ = "PaymentMethods"

    cardNum = Column(Integer)
    transactionStatus = Column(String(50))
    transactionType = Column(String(50))