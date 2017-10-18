-- display records from the database hbtn_0d_usa
-- records are displayed in the cities.id-cities.name-states.name order
SELECT cities.id, cities.name, states.name
       FROM cities
       INNER JOIN states ON cities.state_id=states.id;
