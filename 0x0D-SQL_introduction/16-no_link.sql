-- list all records except rows without a name value from second_table
SELECT score, name
       FROM second_table
       WHERE name IS NOT NULL
       ORDER BY score DESC;
