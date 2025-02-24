from fastapi import FastAPI, HTTPException,Depends
from app.database import Session, engine, Base, get_db
from app.models import Order, OrderCreate, OrderResponse
from typing import List

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.post("/orders", response_model=OrderResponse)
def create_order(order: OrderCreate, db: Session = Depends(get_db)):
    db_order = Order(symbol=order.symbol, price=order.price, quantity=order.quantity, order_type=order.order_type)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    return db_order
    

@app.get("/orders", response_model=List[OrderResponse])
def get_orders(db: Session = Depends(get_db)):
    return db.query(Order).all()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
