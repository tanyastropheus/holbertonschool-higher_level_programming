#!/usr/bin/python3

'''module lists all cities from the database hbtn_0e_4_usa'''

import MySQLdb
import re
from sys import argv

if __name__ == "__main__":
    # open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    # prepare a cursor object using cursor() method
    cur = db.cursor()

    cur.execute(
        "SELECT cities.id, cities.name, states.name\
        FROM cities\
        LEFT JOIN states\
        ON cities.state_id = states.id\
        ORDER BY cities.id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
