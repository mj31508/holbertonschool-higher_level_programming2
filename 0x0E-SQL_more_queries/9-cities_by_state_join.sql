-- script that lists all cities in database

SELECT cities.id, cities.name, states.name
FROM states, cities WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
