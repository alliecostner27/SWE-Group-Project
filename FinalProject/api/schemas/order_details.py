from typing import Optional
from pydantic import BaseModel
from .menu import MenuItem



class OrderDetailBase(BaseModel):
    order_id: int ## Foreign key to order
    quantity: int
    menu_item_id: int ## Foreign key to menuItem


class OrderDetailCreate(OrderDetailBase):
    pass

class OrderDetailUpdate(BaseModel):
    order_id: Optional[int] = None
    menu_item_id: Optional[int] = None
    quantity: Optional[int] = None


class OrderDetail(OrderDetailBase):
    id: int ## Primary Key
    menu_item: MenuItem

    class ConfigDict:
        from_attributes = True