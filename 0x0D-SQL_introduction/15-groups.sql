-- list the number of records with the same score in a table
SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC; 
