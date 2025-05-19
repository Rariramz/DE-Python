-- Rooms with students of different nationalities
SELECT rooms.id, rooms.name, STRING_AGG(DISTINCT students.nationality, ', ') AS nationalities
FROM rooms LEFT JOIN students ON rooms.id = students.room
GROUP BY rooms.id, rooms.name
HAVING COUNT(DISTINCT students.nationality) > 1
