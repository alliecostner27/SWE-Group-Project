from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail
from .customer import Customer
from .review import Review
from .payment_method import PaymentMethod


class OrderBase(BaseModel):
    customer_id: int
    description: Optional[str] = None
    promo_code: Optional[str] = None
    status: str


class OrderCreate(OrderBase):
    order_details: List[OrderDetail]


class OrderUpdate(BaseModel):
    customer_id: Optional[int] = None
    description: Optional[str] = None
    order_details: Optional[List[OrderDetail]] = None


class Order(OrderBase):
    id: int ## Primary Key
    order_date: Optional[datetime] = None
    order_details: list[OrderDetail] = None
    total_price: float = 0
    customer: Customer ## reference full customer object
    reviews: List[Review] = []  ## list of reviews associated with the order
    payment_method: Optional[PaymentMethod] = None

    class ConfigDict:
        from_attributes = True
