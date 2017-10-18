-- displays all the cities of California in the database hbtn_0d_usa
SELECT id, name
       FROM hbtn_0d_usa.cities
       WHERE state_id =
       (SELECT id
       	       FROM cities
	       WHERE name = 'California')
       ORDER BY cities.id ASC;
