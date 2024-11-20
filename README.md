# Fitness Center Management API

A Flask-based RESTful API for managing a fitness center's member database and workout sessions.

## Features

- Member Management (CRUD operations)
- Workout Session Scheduling
- Member Workout History

## Prerequisites

- Python 3.x
- MySQL Server
- Virtual Environment (recommended)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd fitness-center-api
```

2. Create and activate a virtual environment:
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows use: myenv\Scripts\activate
```

3. Install required packages:
```bash
pip install flask mysql-connector-python
```

4. Set up the database:
```bash
mysql -u root -p < create_tables.sql
```

## Configuration

Update the database configuration in `app.py`:
```python
app.config['DB_HOST'] = 'localhost'
app.config['DB_USER'] = 'root'
app.config['DB_PASSWORD'] = 'your_password'
app.config['DB_NAME'] = 'fitness_center'
```

## Running the Application

```bash
python app.py
```
The server will start on `http://localhost:5001`

### Members

1. Create a new member
```bash
POST /members
{
    "name": "John Doe",
    "email": "john@example.com",
    "age": 30
}
```

2. Get member details
```bash
GET /members/<id>
```

3. Update member
```bash
PUT /members/<id>
{
    "name": "John Doe",
    "email": "john@example.com",
    "age": 31
}
```

4. Delete member
```bash
DELETE /members/<id>
```

### Workout Sessions

1. Schedule a workout
```bash
POST /workouts
{
    "member_id": 1,
    "date": "2024-03-19 14:30:00",
    "duration": 60,
    "activity": "cardio"
}
```

2. Update workout session
```bash
PUT /workouts/<id>
{
    "date": "2024-03-19 15:30:00",
    "duration": 45,
    "activity": "strength training"
}
```

3. Get all workouts
```bash
GET /workouts
```

4. Get member's workouts
```bash
GET /members/<id>/workouts
```

## Database Schema

### Members Table
- id (INT, Primary Key)
- name (VARCHAR)
- email (VARCHAR)
- age (INT)
- join_date (TIMESTAMP)

### WorkoutSessions Table
- id (INT, Primary Key)
- member_id (INT, Foreign Key)
- date (DATETIME)
- duration (INT)
- activity (VARCHAR)

## Error Handling

The API includes error handling for:
- Invalid requests
- Database connection issues
- Resource not found
- Duplicate entries
