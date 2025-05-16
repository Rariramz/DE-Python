-- Five rooms with the lowest average student age
SELECT rooms.id, rooms.name, AVG(students.age) as average_age
FROM rooms LEFT JOIN students ON rooms.id = students.room
GROUP BY rooms.id, rooms.name
ORDER BY average_age ASC
LIMIT 5
