from typing import List, Optional
from pydantic import BaseModel
from enum import Enum


class FoodCategoryEnum(str, Enum):
    sandwich = "Sandwich"
    appetizer = "Appetizer"
    main_course = "Main Course"
    dessert = "Dessert"


class MenuItemBase(BaseModel):
    dish_name: str
    ingredients: List[str]
    price: float
    calories: int
    food_category: str


class MenuItemCreate(MenuItemBase):
    pass


class MenuItemUpdate(MenuItemBase):
    dish_name: Optional[str]
    ingredients: Optional[List[str]]
    price: Optional[float]
    calories: Optional[float]
    food_category: Optional[str]


class MenuItem(MenuItemBase):
    id: int ## Primary Key

    class Config:
        from_attributes = True

## menu added as container for multiple menuItem objects
class Menu(BaseModel):
    items: List[MenuItem]

    class ConfigDict:
        from_attributes = True