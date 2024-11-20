from sqlalchemy import Column, ForeignKey, Integer, String, DECIMAL, DATETIME, DOUBLE
from sqlalchemy.orm import relationship
from datetime import datetime
from ..dependencies.database import Base
class MenuDetails(Base):
    __tablename__ = "menu_details"
    
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ingredients = Column(String, index=True, nullable=False)
    price = Column(Double, index=True, nullable=False)
    calories = Column(Integer, index=True, nullable=False)
    food_category = Column(String, index=True, nullable=False)