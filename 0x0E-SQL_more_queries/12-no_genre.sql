-- display tv show titles that do not have a genre linked
-- record is sorted first by tv show titles and then by genre id
SELECT tv_shows.title, tv_show_genres.genre_id
       FROM tv_shows
       LEFT JOIN tv_show_genres
       	     ON tv_shows.id=tv_show_genres.show_id
	     WHERE tv_show_genres.show_id IS NULL
       ORDER BY tv_shows.title, tv_show_genres.genre_id;
