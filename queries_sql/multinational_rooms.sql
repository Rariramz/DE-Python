-- Rooms with students of different nationalities
SELECT rooms.id, rooms.name, students.nationality, STRING_AGG(DISTINCT students.nationality, ', ') AS nationalities
FROM rooms CROSS JOIN students on rooms.id = students.room
GROUP BY rooms.id, rooms.name, students.nationality
HAVING COUNT(DISTINCT students.nationality) > 1
