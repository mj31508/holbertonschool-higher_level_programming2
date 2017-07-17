-- script that lists all the cities in a database

SELECT id, name FROM cities
WHERE state_id in (SELECT id FROM states WHERE name = 'California')
ORDER BY cities.id ASC;
