-- display all genres and the number of shows linked to each
-- genres that do not have any shows linked will not be displayed
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
       FROM tv_show_genres
       LEFT JOIN tv_genres  -- only genres whose id exists in tv_show_genres.genre_id will be displayed
       ON tv_genres.id=tv_show_genres.genre_id
GROUP BY genre
ORDER BY number_shows DESC;
