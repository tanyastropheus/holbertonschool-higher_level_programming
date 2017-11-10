#!/usr/bin/python3

'''module displays data entries that contain matching argument'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # open database connection
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3], charset="utf8")
    # prepare a cursor object using cursor() method
    cur = db.cursor()

    # used '{:s}' inside the ""; code is vulnerable to injection attack
    cur.execute("SELECT * FROM states WHERE name = '{:s}' ORDER BY id ASC".
                format(argv[4]))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()
