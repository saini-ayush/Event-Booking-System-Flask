
# Event Booking System

A Flask-based web application for managing events and bookings.

## Features

- User authentication and authorization
- Event creation and management 
- Booking system for events
- Secure login/logout functionality
- Blueprint-based route organization

## Folder Structure

```
└── 📁eventManagement
    └── 📁app
        └── __init__.py
        └── 📁db
            └── __init__.py
            └── config.py
            └── 📁migration
                └── migration_manager.py
                └── run_migrations.py
                └── 📁versions
                    └── 001_create_users_table.sql
                    └── 002_create_events_table.sql
                    └── 003_create_bookings_table.sql
        └── 📁models
            └── __init__.py
            └── booking.py
            └── event.py
            └── user.py
        └── 📁routes
            └── __init__.py
            └── auth_routes.py
            └── booking_routes.py
            └── event_routes.py
        └── 📁serializers
            └── __init__.py
            └── event_schema.py
            └── user_schema.py
    └── 📁templates
        └── base.html
        └── events.html
        └── login.html
        └── new_event.html
        └── register.html
    └── .env
    └── .gitignore
    └── app.py
    └── config.py
    └── README.md
    └── requirements.txt
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/saini-ayush/Event-Booking-System-Flask.git
cd event-booking-system
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```


4. setup env variables

```bash
FLASK_CONFIG=development
SECRET_KEY=aaaa
DB_NAME=aaaa
DB_USER=postgres
DB_PASSWORD=aaaaa
DB_HOST=localhost
DB_PORT=5433
DATABASE_URL=postgresql://postgres:aaaa@localhost:5433/aaaaa
```

5. Migration

```
python app/db/migrations/run_migrations.py
```

6. Run the application:

```bash
python app.py
```


