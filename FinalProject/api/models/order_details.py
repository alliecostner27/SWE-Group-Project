from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class OrderDetail(Base):
    __tablename__ = "order_details"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)
    menu_item_id = Column(Integer, ForeignKey("menu_items.id"), nullable=False)
    order_type = Column(String(50), nullable=True)

    ## Relationships
    menu_item = relationship("MenuItem")
    order = relationship("Order")
