-- script that removes all records less then 5

select score, name FROM second_table WHERE score <= 5 ORDER BY score DESC;
