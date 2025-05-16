-- List of rooms and the number of students in each room
SELECT rooms.id, rooms.name, COUNT(students.id) AS students_count
FROM rooms LEFT JOIN students ON rooms.id = students.room
GROUP BY rooms.id, rooms.name