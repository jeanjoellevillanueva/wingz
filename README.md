## Project Overview
This is a Django REST Framework project for managing ride information, implementing a comprehensive ride tracking system with advanced filtering, authentication, and performance optimizations.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone git@github.com:jeanjoellevillanueva/wingz.git
cd wingz
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Database Setup
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Create Superuser
```bash
python manage.py createsuperuser
```

### 6. Run Tests
```bash
python manage.py test
```

### 7. Run Server
```bash
python manage.py runserver
```