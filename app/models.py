from sqlalchemy import Boolean, Column, Integer, String, Float
from app.database import Base
from pydantic import BaseModel,validator

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    order_type = Column(String)

class OrderCreate(BaseModel):
    symbol: str
    price: float
    quantity: int
    order_type: str

    @validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Price must be a positive number')
        return value
    
    @validator('quantity')
    def quantity_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Quantity must be greater than 0')
        return value

class OrderResponse(OrderCreate):
    id: int
    symbol: str
    price: float
    quantity: int
    order_type: str


    class Config:
        from_attributes = True