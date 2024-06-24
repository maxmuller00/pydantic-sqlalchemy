from pydantic import BaseModel

class DrinkBase(BaseModel):
    name: str
    description: str | None = None
    price: float
    is_alcohlic: bool

class DrinkCreate(DrinkBase):
    pass

class Drink(DrinkBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class ItemBase(BaseModel):
    title: str
    description: str | None = None

class ItemCreate(ItemBase):
    pass

class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    email: str

class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True

