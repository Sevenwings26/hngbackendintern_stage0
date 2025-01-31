# Basic Profile API

## Description
This project is a FastAPI-based API for managing user profiles. It provides endpoints for retrieving basic API information and user profiles. The API supports CORS handling to allow cross-origin requests from frontend applications.

## Tech Stack
- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **SQLAlchemy**: ORM used for database interactions.
- **Asyncpg**: PostgreSQL driver for async database interactions.
- **PostgreSQL**: A relational database to store profile data.
- **Pydantic**: Data validation and serialization for request/response models.

## Setup Instructions
### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Installation Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/Sevenwings26/hngbackendintern_stage0/
   cd project_directory
   ```

2. **Create a Virtual Environment and Activate It**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   source venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**
   Create a `.env` file and configure necessary environment variables:
   ```env
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname   (for production)
     or
   DATABASE_URL=sqlite:///./profile5.db (for development)
   ```

5. **Run the FastAPI Server**
   ```bash
   uvicorn main:app --reload
   ```

6. **Access the API**
   - Open your browser and visit: [http://127.0.0.1:8000](http://127.0.0.1:8000)
   - API documentation is available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## API Documentation
### Base URL
```
http://127.0.0.1:8000
```

### Endpoints
#### 1. Get API Information
- **URL:** `/`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "message": "FastAPI with CORS enabled",
    "Documentation": "/docs/",
    "Profile": "/profile/"
  }
  ```

#### 2. Get Profile Information
- **URL:** `/profile/`
- **Method:** `GET`
- **Response:**
  ```json
  {
    "email": "iarowosola25@gmail.com",
    "current_datetime": "2025:01:31:19:23:0000",
    "github_url": "https//:github.com/sevenwings"
  }
  ```

#### 3. Create Profile 
- **URL:** `/create/`
- **Method:** `POST`
- **Response:**
  ```json
  {
    "name":"Iyanu Arowosola",
    "email": "iarowosola25@gmail.com",
    "current_datetime": "2025:01:31:19:23:0000",
    "github_url": "https//:github.com/sevenwings"
  }
  ```


### Example Usage
Fetch profile information using `curl`:
```bash
curl -X GET "http://127.0.0.1:8000/profile/" -H "accept: application/json"
```

## CORS Handling
This API includes CORS support to allow cross-origin requests. The `CORSMiddleware` has been configured to permit requests from specified origins, methods, and headers.

## Hiring Python Developers
Looking to hire expert Python developers? Check out [HNG Python Developers](https://hng.tech/hire/python-developers).
