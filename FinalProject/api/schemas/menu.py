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
    food_category: FoodCategoryEnum

class MenuItemCreate(MenuItemBase):
    pass

class MenuItemUpdate(BaseModel):
    dish_name: Optional[str] = None
    ingredients: Optional[List[str]] = None
    price: Optional[float] = None
    calories: Optional[int] = None
    food_category: Optional[FoodCategoryEnum] = None

class MenuItem(MenuItemBase):
    id: int

    class Config:
        from_attributes = True

class Menu(BaseModel):
    items: List[MenuItem]

    class Config:
        from_attributes = True