# User API

A RESTful API service for managing users with the ability to select a repository (in-memory or database) during application initialization. The project is developed using **FastAPI**, **PostgreSQL**, **SQLAlchemy**, and **Docker Compose**. Tests are written using **pytest**.

## Table of Contents

- [Requirements](#requirements)
- [Installation and Setup](#installation-and-setup)
  - [Clone the Repository](#clone-the-repository)
  - [Start the Database](#start-the-database)
  - [Configure the Application](#configure-the-application)
  - [Run the Application](#run-the-application)
- [API Usage](#api-usage)
  - [Swagger Documentation](#swagger-documentation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)


## Requirements

- Python 3.10 or higher
- Docker and Docker Compose
- PostgreSQL (if using the database repository)

## Installation and Setup

### Clone the Repository

```bash
git clone https://github.com/sixtis1/test-crud.git
cd test-crud
```

### Clone the Repository
Install the dependencies from the requirements.txt file:
```bash
pip install -r requirements.txt
```

### Start the Database
Start the PostgreSQL container using Docker Compose:
```bash
docker-compose up -d
```

### Configure the Application

Configuration parameters are located in the app/.env file.
```env
REPOSITORY_TYPE=memory # Change to "db" to use the database repository
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/test_db

POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=test_db
```

### Run the Application
Start the application using Uvicorn:
```bash
python -m uvicorn app.main:app --reload
```
The application will be available at: http://localhost:8000

Upon startup, the application automatically creates the necessary tables in the database.

## API Usage

### Swagger Documentation
Interactive API documentation is available at http://localhost:8000/docs

## Running Tests
Execute the following command to run all tests:
```bash
pytest
```

## Project Structure

```bash
├── app
│   ├── __init__.py
│   ├── main.py                # Entry point of the FastAPI application
│   ├── user_model.py              # SQLAlchemy models
│   ├── schema.py             # Pydantic schema for validation
│   ├── routers
│   │   ├── __init__.py
│   │   └── users.py           # Endpoints for user operations
│   ├── repositories
│   │   ├── __init__.py
│   │   ├── base.py            # Abstract repository class
│   │   ├── memory_repository.py  # In-memory repository implementation
│   │   └── db_repository.py   # Database repository implementation
│   ├── dependencies.py        # Application dependencies
│   └── config.py              # Configuration file
├── tests
│   ├── __init__.py
│   └── test_users.py          # Tests for user endpoints
├── docker-compose.yml         # Docker Compose file for PostgreSQL
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```
