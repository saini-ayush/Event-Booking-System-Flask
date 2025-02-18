
# Event Booking System

A Flask-based web application for managing events and bookings.

## Features

- User authentication and authorization
- Event creation and management 
- Booking system for events
- Secure login/logout functionality
- Blueprint-based route organization

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

5. Run the application:

```bash
python app.py
```


