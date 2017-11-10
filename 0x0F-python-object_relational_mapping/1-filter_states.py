#!/usr/bin/python3
'''module displays data entries starting with N
'''

import MySQLdb
import re
from sys import argv

if __name__ == "__main__":
    # open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    # prepare a cursor object using cursor() method
    cur = db.cursor()

    # using MySQL regexp to select entries whose names start with N
    cur.execute("SELECT * FROM states WHERE name REGEXP '^N' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
