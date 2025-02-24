# Order Management API

## Overview
This project is a simple backend service that provides a REST API for managing stock trade orders. The application is built using **FastAPI (Python)** and supports creating and retrieving stock orders. It is containerized with **Docker**, deployed on **AWS EC2**, and utilizes **GitHub Actions** for CI/CD automation.

## Public Endpoint
This API is publicly accessible at the following domain: http://3.147.79.90/orders 

### Example Requests
#### Create a New Order (POST Request)
**Endpoint:** `POST http://3.147.79.90/orders`

**Request Body:**
```json
{
    "symbol": "SYHG",
    "price": 45.24,
    "quantity": 13,
    "order_type": "sell"
}
```

**Response:**
```json
{
    "id": 2,
    "symbol": "SYHG",
    "price": 45.24,
    "quantity": 13,
    "order_type": "sell"
}
```

#### Retrieve All Orders (GET Request)
**Endpoint:** `GET http://3.147.79.90/orders`

**Response:**
```json
[
  {
    "id": 1,
    "symbol": "AAPL",
    "price": 150.5,
    "quantity": 10,
    "order_type": "buy"
  },
  {
    "id": 2,
    "symbol": "SYHG",
    "price": 45.24,
    "quantity": 13,
    "order_type": "sell"
  }
]
```

## Features
- **RESTful API** for order creation and retrieval.
- **Persistent storage** using PostgreSQL (or SQLite for simplicity).
- **Containerized deployment** with Docker.
- **CI/CD pipeline** using GitHub Actions for automated testing, building, and deployment.
- **WebSocket support (Bonus)** for real-time order updates.
- **Unit Tests** ensuring reliability of API endpoints.

## Technologies Used
- **Backend**: Python (FastAPI)
- **Database**: PostgreSQL / SQLite
- **Containerization**: Docker, Docker Compose
- **Deployment**: AWS EC2 (Ubuntu)
- **CI/CD**: GitHub Actions
- **Testing**: Pytest

---

## API Endpoints
### 1. Create a New Order
**Endpoint:** `POST /orders`

**Request Body:**
```json
{
  "symbol": "AAPL",
  "price": 150.5,
  "quantity": 10,
  "order_type": "buy"
}
```

**Response:**
```json
{
  "id": 1,
  "symbol": "AAPL",
  "price": 150.5,
  "quantity": 10,
  "order_type": "buy"
}
```

---

### 2. Retrieve All Orders
**Endpoint:** `GET /orders`

**Response:**
```json
[
  {
    "id": 1,
    "symbol": "AAPL",
    "price": 150.5,
    "quantity": 10,
    "order_type": "buy"
  }
]
```

---

## Database Schema
### Order Table
| Column      | Type    | Description                   |
|------------|--------|-------------------------------|
| id         | INT    | Unique order ID               |
| symbol     | STRING | Stock ticker symbol           |
| price      | FLOAT  | Price per stock               |
| quantity   | INT    | Number of stocks              |
| order_type | STRING | Type of order ('buy'/'sell')  |

---

## Setup and Installation

### 1. Clone the Repository
```sh
git clone https://github.com/RonaldRommel/order-management-api.git
cd order-management-api
```

### 2. Set Up Virtual Environment (Optional)
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

### 4. Run the API Locally
```sh
uvicorn main:app 
```

The API will be available at `http://localhost:8000`

### 5. Run Unit Tests
```sh
pytest
```

---

## Docker Setup
### 1. Build and Run Docker Container
```sh
docker build -t blockhouse .
docker run -d -v ./data:/code/data -p 80:8000 blockhouse
```

### 2. Deploy on AWS EC2
1. Launch an EC2 instance (Ubuntu).
2. Install Docker and PostgreSQL.
3. Copy the project files to the server.
4. Run the Docker container.

---

## CI/CD Pipeline
The GitHub Actions workflow automates:
1. Running unit tests on pull requests.
2. Building the Docker container.
3. SSH deployment to AWS EC2 upon merging to `main`.

Workflow configuration is in `.github/workflows/main.yml`.

---

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

## Author
Ronald Rommel Myloth

Email: [mylothronald@gmail.com](mailto:mylothronald@gmail.com)

