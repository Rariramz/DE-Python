DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS rooms;

CREATE TABLE IF NOT EXISTS rooms (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS students (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT NOT NULL CHECK (age >= 0),
    room INT NOT NULL REFERENCES rooms(id),
    sex CHAR(1) NOT NULL CHECK (sex IN ('F', 'M')),
    nationality VARCHAR(255) NOT NULL
);

CREATE INDEX idx_students_room_age ON students (room, age);
CREATE INDEX idx_students_room_nationality ON students (room, nationality);
