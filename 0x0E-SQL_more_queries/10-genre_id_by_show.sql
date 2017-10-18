-- display records containing tv show titles and genre id
-- record is sorted first by tv show titles and then by genre id
SELECT tv_shows.title, tv_show_genres.genre_id
       FROM tv_shows
       INNER JOIN tv_show_genres
       	     ON tv_shows.id=tv_show_genres.show_id
       ORDER BY tv_shows.title, tv_show_genres.genre_id;
