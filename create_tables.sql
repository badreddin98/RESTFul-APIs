CREATE DATABASE IF NOT EXISTS fitness_center;
USE fitness_center;

CREATE TABLE IF NOT EXISTS Members (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    age INT,
    join_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS WorkoutSessions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    member_id INT NOT NULL,
    date DATETIME NOT NULL,
    duration INT NOT NULL,
    activity VARCHAR(100) NOT NULL,
    FOREIGN KEY (member_id) REFERENCES Members(id)
);