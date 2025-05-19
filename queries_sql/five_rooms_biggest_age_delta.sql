-- Five rooms with the highest age difference
SELECT rooms.id, rooms.name, MAX(students.age) - MIN(students.age) as age_delta
FROM rooms LEFT JOIN students ON rooms.id = students.room
GROUP BY rooms.id, rooms.name
ORDER BY age_delta DESC
LIMIT 5
