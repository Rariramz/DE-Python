DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS rooms;

CREATE TABLE IF NOT EXISTS rooms (
    id INT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT,
    room INT,
    sex CHAR(1),
    nationality VARCHAR(255),
    FOREIGN KEY (room) REFERENCES rooms(id)
);
