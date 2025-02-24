from sqlalchemy import Boolean, Column, Integer, String, Float
from src.database import Base
from pydantic import BaseModel, Field, field_validator
import re

class Order(Base):
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    symbol = Column(String, index=True)
    price = Column(Float)
    quantity = Column(Integer)
    order_type = Column(String)

class OrderCreate(BaseModel):
    symbol: str = Field(..., example="AAPL", description="Stock ticker symbol (1-5 uppercase letters)")
    price: float = Field(..., gt=0, example=150.5, description="Price per stock (must be positive)")
    quantity: int = Field(..., gt=0, example=10, description="Number of stocks (must be positive)")
    order_type: str = Field(..., example="buy", description="Type of order ('buy' or 'sell')")

    @field_validator('price')
    def price_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Price must be a positive number')
        return value
    
    @field_validator('quantity')
    def quantity_must_be_positive(cls, value):
        if value <= 0:
            raise ValueError('Quantity must be greater than 0')
        return value

    @field_validator("symbol")
    def validate_ticker_symbol(cls, symbol):
        if not re.match(r"^[A-Z]{1,5}$", symbol):
            raise ValueError("Invalid stock symbol. It must be 1-5 uppercase letters.")
        return symbol

class OrderResponse(OrderCreate):
    id: int = Field(..., example=1, description="Unique order ID")

    class Config:
        from_attributes = True
