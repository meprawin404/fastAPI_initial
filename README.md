# Bikes API - FastAPI Application

A simple RESTful API for managing bikes using FastAPI, SQLAlchemy, and SQLite database.

## 🚀 Features

- **CRUD Operations**: Create, Read, Update, Delete bikes
- **Database**: SQLite database with SQLAlchemy ORM
- **Interactive Docs**: Automatic API documentation with Swagger UI
- **Data Validation**: Pydantic models for request/response validation
- **Dependency Injection**: Database session management

## 📋 Prerequisites

- Python 3.8+
- pip (Python package manager)

## 🛠️ Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd FastApiBasic
   ```

2. **Create virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   uvicorn main:app --reload
   ```

5. **Access the API**
   - API Base URL: `http://127.0.0.1:8000`
   - Interactive Docs: `http://127.0.0.1:8000/docs`
   - Alternative Docs: `http://127.0.0.1:8000/redoc`

## 📊 Database Schema

### Bikes Table
| Column | Type    | Description                    |
|--------|---------|--------------------------------|
| id     | Integer | Primary key, auto-increment    |
| name   | String  | Name of the bike (indexed)     |
| brand  | String  | Brand of the bike              |

## 📁 Project Structure

```
FastApiBasic/
├── main.py          # FastAPI application and routes
├── models.py        # SQLAlchemy database models
├── database.py      # Database configuration
├── requirements.txt # Python dependencies
├── bikes.db         # SQLite database file (auto-generated)
└── README.md        # Project documentation
```

## 🔧 API Endpoints

### 1. Welcome Message
**GET** `/`

Returns a welcome message.

**Response:**
```json
{
  "msg": "welcome to Bikers"
}
```

---

### 2. Get All Bikes
**GET** `/bikes`

Retrieves all bikes from the database.

**Response:**
```json
[
  {
    "id": 1,
    "name": "Mountain Bike",
    "brand": "Trek"
  },
  {
    "id": 2,
    "name": "Road Bike",
    "brand": "Giant"
  }
]
```

**Response Model:** `List[BikeResponse]`

---

### 3. Create New Bike
**POST** `/bikes`

Creates a new bike in the database.

**Request Body:**
```json
{
  "name": "Mountain Bike",
  "brand": "Trek"
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Mountain Bike",
  "brand": "Trek"
}
```

**Request Model:** `BikeCreate`
**Response Model:** `BikeResponse`

---

## 📝 Data Models

### BikeCreate (Request Model)
Used for creating new bikes (POST requests).

```python
{
  "name": "string",    # Required: Name of the bike
  "brand": "string"    # Required: Brand of the bike
}
```

### BikeResponse (Response Model)
Used for API responses.

```python
{
  "id": "integer",     # Auto-generated ID
  "name": "string",    # Name of the bike
  "brand": "string"    # Brand of the bike
}
```

## 🧪 Testing the API

### Using curl

1. **Get all bikes:**
   ```bash
   curl -X GET "http://127.0.0.1:8000/bikes"
   ```

2. **Create a new bike:**
   ```bash
   curl -X POST "http://127.0.0.1:8000/bikes" \
        -H "Content-Type: application/json" \
        -d '{"name": "Mountain Bike", "brand": "Trek"}'
   ```

### Using Python requests

```python
import requests

# Get all bikes
response = requests.get("http://127.0.0.1:8000/bikes")
print(response.json())

# Create a new bike
new_bike = {"name": "Road Bike", "brand": "Giant"}
response = requests.post("http://127.0.0.1:8000/bikes", json=new_bike)
print(response.json())
```

### Using Interactive Documentation

Visit `http://127.0.0.1:8000/docs` for Swagger UI where you can:
- View all endpoints
- Test API calls directly in the browser
- See request/response schemas
- Download OpenAPI specification

## 🗃️ Database

- **Type**: SQLite
- **File**: `bikes.db` (auto-created)
- **ORM**: SQLAlchemy
- **Session Management**: Dependency injection with automatic cleanup

The database is automatically created when you first run the application.

## 🔧 Configuration

### Database Configuration (`database.py`)
- **Database URL**: `sqlite:///./bikes.db`
- **Connection**: SQLite with thread safety disabled
- **Session**: Non-autocommit, non-autoflush

### Dependencies
Key packages used:
- `fastapi`: Web framework
- `uvicorn`: ASGI server
- `sqlalchemy`: ORM
- `pydantic`: Data validation

## 🚀 Future Enhancements

Potential improvements for this API:

- [ ] Add UPDATE endpoint (PUT `/bikes/{bike_id}`)
- [ ] Add DELETE endpoint (DELETE `/bikes/{bike_id}`)
- [ ] Add GET single bike endpoint (GET `/bikes/{bike_id}`)
- [ ] Add search and filtering capabilities
- [ ] Add authentication and authorization
- [ ] Add pagination for large datasets
- [ ] Add input validation and error handling
- [ ] Add logging and monitoring
- [ ] Add unit and integration tests
- [ ] Add API versioning
- [ ] Add rate limiting

## 📜 License

This project is open source and available under the [MIT License](LICENSE).


