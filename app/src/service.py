from fastapi import FastAPI, HTTPException, Depends
from src.database import Session, engine, Base, get_db
from src.models import Order, OrderCreate, OrderResponse
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Order Management API",
    description="An API to create and fetch stock orders",
    version="1.0.0",
    contact={
        "name": "Ronald Rommel Myloth",
        "email": "mylothronald@gmail.com",
    },
    license_info={
        "name": "MIT License",
        "url": "https://opensource.org/licenses/MIT",
    }
)

@app.post("/orders", response_model=OrderResponse, summary="Create a new stock order", tags=["Orders"])
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    """
    **Creates a new order** in the system.

    - **symbol**: Stock ticker symbol (e.g., "AAPL", "TSLA")
    - **price**: Price per stock
    - **quantity**: Number of stocks
    - **order_type**: "buy" or "sell"

    Returns the created order details.
    """
    db_order = Order(symbol=order.symbol, price=order.price, quantity=order.quantity, order_type=order.order_type)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
    

@app.get("/orders", response_model=List[OrderResponse], summary="Get all orders", tags=["Orders"])
def get_orders(db: Session = Depends(get_db)):
    """
    **Fetches all orders** from the system.

    Returns a list of all stock orders.
    """
    return db.query(Order).all()
