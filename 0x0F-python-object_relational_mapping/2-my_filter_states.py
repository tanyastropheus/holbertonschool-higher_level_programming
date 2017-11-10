#!/usr/bin/python3
import MySQLdb
import re
from sys import argv
# open database connection
db = MySQLdb.connect(host="localhost", port=3306, user=argv[1], passwd=argv[2],
                     db=argv[3], charset="utf8")

# prepare a cursor object using cursor() method
cur = db.cursor()

# format WHERE with list of arguments and %s
cur.execute("SELECT * FROM states WHERE name = %s", [argv[4]])
data = cur.fetchone()
print(data)
cur.close()
db.close()
