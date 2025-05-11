# Django + FastAPI User Management System

This is a minimal user management system built with Django (admin, ORM) and FastAPI (REST API), using SQLite as the database.

---

## Features

- Django Admin interface for managing users
- FastAPI REST API:
  - `GET /users/`: List all users
  - `GET /users/{id}`: Retrieve a user by UUID
  - `POST /users/`: Create a new user
  - `PUT /users/{id}`: Update an existing user
  - `DELETE /users/{id}`: Soft delete (set `is_active=False`)
- Pydantic for request/response validation
- Dummy data generation with Faker

---

## Setup Instructions

### 1. Clone the Repository
git clone https://sureshs11593/user_management_accessment.git;
cd user_mgmt_project

### 2. setup virtual environment and installing required module
python -m venv venv;
venv\Scripts\activate;
pip install -r requirements.txt;

### 3. Apply Migrations
python manage.py makemigrations;
python manage.py migrate;

### 4. Create SuperUser/admin [Optional]
python manage.py createsuperuser;

### 5. Populate dummy users
python manage.py populate_users;

### 6.  Run Django Admin
python manage.py runserver; **--> you can visit /admin to verify admin access**

### 7. Run Fast API app
uvicorn fastapi_app.main:app --reload; **--> can be accessed using /docs**

