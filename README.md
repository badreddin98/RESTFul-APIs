# Fitness Center Management API

This Flask application provides a RESTful API for managing a fitness center's database, including member management and workout session tracking.

## Setup Instructions

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure the database:
- Create a MySQL database named `fitness_center`
- Update the `.env` file with your database credentials

4. Run the application:
```bash
python app.py
```

## API Endpoints

### Members

- **POST /members** - Add a new member
  ```json
  {
    "name": "John Doe",
    "email": "john@example.com",
    "membership_type": "premium"
  }
  ```

- **GET /members** - Get all members
- **GET /members/{id}** - Get a specific member
- **PUT /members/{id}** - Update a member
- **DELETE /members/{id}** - Delete a member

### Workout Sessions

- **POST /workout-sessions** - Schedule a new workout session
  ```json
  {
    "member_id": 1,
    "date": "2023-09-20 14:30:00",
    "workout_type": "cardio",
    "duration": 60
  }
  ```

- **GET /members/{member_id}/workout-sessions** - Get all workout sessions for a member
- **PUT /workout-sessions/{id}** - Update a workout session
- **DELETE /workout-sessions/{id}** - Delete a workout session
