from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, CheckConstraint
from sqlalchemy.orm import relationship

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True, index = True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
    drinks = relationship("Drink", back_populates="owner")

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="items")

class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float, index=True)
    is_alcoholic = Column(Boolean, default=True)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="drinks")

    __table_args__ = (
        CheckConstraint('price >= 1 AND price <= 30', name='check_price_range'),
    )