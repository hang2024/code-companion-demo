# Code Companion Demo

This repository hosts a full-stack application with an Angular frontend and Django backend, showcasing basic CRUD operations integrated with a PostgreSQL database.

## Prerequisites

To run this project, you will need:

- [Node.js and npm](https://nodejs.org/en/download/)
- [Python 3](https://www.python.org/downloads/)
- [PostgreSQL](https://www.postgresql.org/download/)

## Installation

### Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/hang2024/code-companion-demo.git
cd code-companion-demo
```

## PostgreSQL Setup

Create a database and user using either psql or pgAdmin:

sql example using psql:

```sql
psql -U postgres
CREATE DATABASE postgres;
CREATE USER postgres WITH ENCRYPTED PASSWORD '123';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
\q
```

Update the Django `settings.py` file:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '123',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

### Backend Setup

Set up and run the Django backend:

```bash
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Unix/MacOS
pip install -r requirements.txt
cd DjangoRestApisPostgreSQL
python manage.py migrate
python manage.py runserver 8080
```

### Frontend Setup

Set up and run the Angular frontend:

```bash
cd ../frontend
npm install
ng serve --port 8081
```

## Usage

Access the frontend at `http://localhost:8081` and the backend at `http://localhost:8080`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
