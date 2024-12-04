import string
from typing import Optional
from pydantic import BaseModel
from .menu import MenuItem


class OrderDetailBase(BaseModel):
    quantity: int
    menu_item_id: int ## Foreign key to menuItem
    order_type: str


class OrderDetailCreate(OrderDetailBase):
    pass


class OrderDetailUpdate(OrderDetailBase):
    pass


class OrderDetail(OrderDetailBase):
    id: int ## Primary Key

    class ConfigDict:
        from_attributes = True