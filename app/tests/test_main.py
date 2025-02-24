import pytest
from fastapi import FastAPI, HTTPException,Depends
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.database import Base, get_db
from src.service import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./data/test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

Base.metadata.create_all(bind=engine)

client = TestClient(app)

sample_order = {
    "symbol": "AAPL",
    "price": 150.5,
    "quantity": 10,
    "order_type": "buy"
}

def test_create_order():
    """Test order creation"""
    response = client.post("/orders", json=sample_order)
    assert response.status_code == 200
    data = response.json()
    assert data["symbol"] == sample_order["symbol"]
    assert data["price"] == sample_order["price"]
    assert data["quantity"] == sample_order["quantity"]
    assert data["order_type"] == sample_order["order_type"]
    assert "id" in data  

def test_get_orders():
    """Test retrieving all orders"""
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    sample_order = {
        "symbol": "AMZN",
        "price": 3300.0,
        "quantity": 10, 
        "order_type": "buy"
    }
    client.post("/orders", json=sample_order)
    response = client.get("/orders")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0  
    assert data[0]["symbol"] == sample_order["symbol"]

def test_invalid_order_symbol():
    """Test creating an order with an invalid stock symbol"""
    invalid_order = {
        "symbol": "INVALID123",  
        "price": 200.0,
        "quantity": 5,
        "order_type": "sell"
    }
    response = client.post("/orders", json=invalid_order)
    assert response.status_code == 422  

def test_invalid_price():
    """Test order creation with invalid price"""
    invalid_order = {
        "symbol": "TSLA",
        "price": -10.0,  
        "quantity": 5,
        "order_type": "sell"
    }
    response = client.post("/orders", json=invalid_order)
    assert response.status_code == 422 

def test_invalid_quantity():
    """Test order creation with invalid quantity"""
    invalid_order = {
        "symbol": "AMZN",
        "price": 3300.0,
        "quantity": 0, 
        "order_type": "buy"
    }
    response = client.post("/orders", json=invalid_order)
    assert response.status_code == 422  
