-- list all records except rows without a name value from second_table
SELECT score, name
       WHERE name = ''
       ORDER BY score DESC;
