from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
from ..dependencies.database import Base

class MenuItem(Base):
    __tablename__ = "menu_items"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    dish_name = Column(String(100), nullable=False)
    ingredients = Column(String(255), nullable=False)  # Consider storing as a comma-separated string or using a separate table for ingredients
    price = Column(Float, nullable=False)
    calories = Column(Integer, nullable=False)
    food_category = Column(String(50), nullable=False)  # You could also use an Enum type if supported by your database

    # Relationships
    menu_id = Column(Integer, ForeignKey('menus.id'), nullable=True)  # Assuming a menus table exists
    menu = relationship("Menu", back_populates="items")  # Establishing a relationship with Menu


class Menu(Base):
    __tablename__ = "menus"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)

    # Relationships
    items = relationship("MenuItem", back_populates="menu", lazy='dynamic')  # Establishing a relationship with MenuItem
