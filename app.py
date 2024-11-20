from flask import Flask, request, jsonify
import mysql.connector

app = Flask(__name__)

# Database configuration
app.config['DB_HOST'] = 'localhost'
app.config['DB_USER'] = 'root'
app.config['DB_PASSWORD'] = '1q2w3e4r5t6y'  # If you have a password, add it here
app.config['DB_NAME'] = 'fitness_center'

# Database connection function
def get_db_connection():
    return mysql.connector.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        database=app.config['DB_NAME']
    )

# Task 2: CRUD operations for Members
@app.route('/members', methods=['POST'])
def add_member():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO Members (name, age, email) VALUES (%s, %s, %s)",
            (data['name'], data['age'], data['email'])
        )
        connection.commit()
        return jsonify({'message': 'Member added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/members/<int:id>', methods=['GET'])
def get_member(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Members WHERE id = %s", (id,))
        member = cursor.fetchone()
        if member:
            return jsonify(member), 200
        else:
            return jsonify({'error': 'Member not found'}), 404
    finally:
        cursor.close()
        connection.close()

@app.route('/members/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "UPDATE Members SET name = %s, age = %s, email = %s WHERE id = %s",
            (data['name'], data['age'], data['email'], id)
        )
        connection.commit()
        if cursor.rowcount:
            return jsonify({'message': 'Member updated successfully'}), 200
        else:
            return jsonify({'error': 'Member not found'}), 404
    finally:
        cursor.close()
        connection.close()

@app.route('/members/<int:id>', methods=['DELETE'])
def delete_member(id):
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute("DELETE FROM Members WHERE id = %s", (id,))
        connection.commit()
        if cursor.rowcount:
            return jsonify({'message': 'Member deleted successfully'}), 200
        else:
            return jsonify({'error': 'Member not found'}), 404
    finally:
        cursor.close()
        connection.close()

# Task 3: Managing Workout Sessions
@app.route('/workouts', methods=['POST'])
def schedule_workout():
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "INSERT INTO WorkoutSessions (member_id, date, duration, activity) VALUES (%s, %s, %s, %s)",
            (data['member_id'], data['date'], data['duration'], data['activity'])
        )
        connection.commit()
        return jsonify({'message': 'Workout session scheduled successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        cursor.close()
        connection.close()

@app.route('/workouts/<int:id>', methods=['PUT'])
def update_workout(id):
    data = request.json
    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(
            "UPDATE WorkoutSessions SET date = %s, duration = %s, activity = %s WHERE id = %s",
            (data['date'], data['duration'], data['activity'], id)
        )
        connection.commit()
        if cursor.rowcount:
            return jsonify({'message': 'Workout session updated successfully'}), 200
        else:
            return jsonify({'error': 'Workout session not found'}), 404
    finally:
        cursor.close()
        connection.close()

@app.route('/workouts', methods=['GET'])
def get_workouts():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM WorkoutSessions")
        workouts = cursor.fetchall()
        return jsonify(workouts), 200
    finally:
        cursor.close()
        connection.close()

@app.route('/members/<int:id>/workouts', methods=['GET'])
def get_member_workouts(id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM WorkoutSessions WHERE member_id = %s", (id,))
        workouts = cursor.fetchall()
        return jsonify(workouts), 200
    finally:
        cursor.close()
        connection.close()

if __name__ == '__main__':
    app.run(debug=True, port=5001)
