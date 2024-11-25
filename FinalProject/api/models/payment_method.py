from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from ..dependencies.database import Base
from enum import Enum as PyEnum

class TransactionStatus(PyEnum):
    pending = 'pending'
    approved = 'approved'
    failed = 'failed'


class TransactionType(PyEnum):
    debit = 'debit'
    credit = 'credit'


class PaymentMethod(Base):
    __tablename__ = "payment_methods"

    id = Column(Integer, primary_key=True,index = True, autoincrement=True)
    card_num = Column(String(20), nullable=False)
    transaction_status = Column(Enum(TransactionStatus), nullable=False)
    transaction_type = Column(Enum(TransactionType), nullable=False)

    ## Relationships
    orders = relationship("Order", back_populates="payment_method")
