from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class Review(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    review = Column(String(500), nullable=False)
    score = Column(Integer, nullable=False)

    # Relationships
    order = relationship("Order", back_populates="reviews")
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=True)
    customer = relationship("Customer", back_populates="reviews")
