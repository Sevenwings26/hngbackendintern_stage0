# Profile API with FastAPI & PostgreSQL

## Project Overview

This project is a project given by HNG12 stage0 - A public API to retrieve Basic Information. I used **FastAPI** application that interacts with a **PostgreSQL** database. It allows users to create and retrieve profile data. 

## Features

- **Create Profile**: A `POST` endpoint that allows users to create profiles.
- **Retrieve First Profile**: A `GET` endpoint that retrieves the first profile from the database.
- **Datetime Management**: The `current_datetime` field handles `datetime` objects, which are saved in the database as either **ISO 8601 formatted timestamps** or **naive datetime** (without timezone).

## Tech Stack

- **FastAPI**: A modern, fast web framework for building APIs with Python.
- **SQLAlchemy**: ORM used for database interactions.
- **Asyncpg**: PostgreSQL driver for async database interactions.
- **PostgreSQL**: A relational database to store profile data.
- **Pydantic**: Data validation and serialization for request/response models.

## Requirements

- Python 3.10+
- `FastAPI`
- `SQLAlchemy`
- `asyncpg`
- `PostgreSQL`
- `Pydantic`

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Sevenwings26/hngbackendintern_stage0
    cd profile-api
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv venv
    venv\Scripts\activate  # For Windows use: source venv/bin/activate  
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```
    

## Database Configuration

The application uses **SQLAlchemy** and **asyncpg** for asynchronous database interactions. The `Profile` model includes a `current_datetime` field, which is stored as an **ISO 8601 formatted timestamp** or (**naive datetime** - without timezone) based on your configuration.

### Handling DateTime

To resolve issues related to datetime storage:

1. **Naive datetime (without timezone):**

   If you wish to store `current_datetime` as a **naive datetime** (timezone-naive), ensure the datetime object is **timezone-aware** before storing it. This can be done by replacing the `tzinfo` with `None`.

   Example fix in `create_profile`:

   ```python
   naive_datetime = profile_data.current_datetime.replace(tzinfo=None)
