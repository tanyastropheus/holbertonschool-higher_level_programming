-- display all genres and the number of shows linked to each
-- genres that do not have any shows linked will not be displayed
SELECT tv_genres.name, COUNT(tv_show_genres.genre_id) AS number_shows
       FROM tv_show_genres
       LEFT JOIN tv_genres
       ON tv_genres.id=tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_shows DESC;
