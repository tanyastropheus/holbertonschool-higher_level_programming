#!/usr/bin/python3

'''module lists all cities from a specified state'''

import MySQLdb
import re
from sys import argv

if __name__ == "__main__":
    # open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    # prepare a cursor object using cursor() method
    cur = db.cursor()

    # format WHERE with %s and a list of argument (substitution)
    cur.execute(
        "SELECT cities.name\
        FROM cities\
        LEFT JOIN states\
        ON cities.state_id = states.id\
        WHERE states.name = %s\
        ORDER BY cities.id", (argv[4],))

    query_rows = cur.fetchall()

    # format the print output
    flag = True
    for row in query_rows:
        if flag is True:
            print("{}".format(row[0]), end="")
            flag = False
        else:
            print(", {}".format(row[0]), end="")
    print("")

    cur.close()
    db.close()
