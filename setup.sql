CREATE DATABASE IF NOT EXISTS hostel_management;
USE hostel_management;

CREATE TABLE IF NOT EXISTS rooms (
    room_no INT PRIMARY KEY,
    capacity INT NOT NULL,
    occupied INT DEFAULT 0
);

CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    room_no INT,
    FOREIGN KEY (room_no) REFERENCES rooms(room_no)
);
