-- extra credit

SELECT DISTINCT tv_genres. name FROM tv_genres
WHERE tv_genres.id NOT IN (SELECT DISTINCT t.genre_id FROM tv_show_genres t
INNER JOIN tv_shows u ON u.id = t.show_id
INNER JOIN tv_genres v ON t.genre_id = v.id
WHERE u. title = Dexter)
ORDER BY tv_genres. NAME ASC;
