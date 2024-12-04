from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel
from .order_details import OrderDetail
from .customer import Customer
from .review import Review
from .payment_method import PaymentMethod


class OrderBase(BaseModel):
    order_date: Optional[datetime] = None
    order_detail_id: int ## reference order detail entry
    total_price: float = 0
    customer_id: int  ## reference full customer entry
    payment_method_id: Optional[int]


class OrderCreate(OrderBase):
    pass


class OrderUpdate(OrderBase):
    pass


class Order(OrderBase):
    id: int ## Primary Key

    class ConfigDict:
        from_attributes = True
