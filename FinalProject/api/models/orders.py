from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    order_date = Column(DATETIME, nullable=False, server_default=str(datetime.now()))
    total_price = Column(DECIMAL(10, 2), default=0.00)
    payment_method_id = Column(Integer, ForeignKey('payment_methods.id'), nullable=False)
    order_detail_id = Column(Integer, ForeignKey('order_details.id'), nullable=False)
    review_id = Column(Integer, ForeignKey('reviews.id'), nullable=True)

    ## Relationships
    customer = relationship("customers.id", back_populates="orders")
    order_details = relationship("order_details.id", back_populates="orders")
    review = relationship("reviews.id", back_populates="orders", lazy="dynamic")
    payment_method = relationship("payment_methods.id", back_populates="orders")

