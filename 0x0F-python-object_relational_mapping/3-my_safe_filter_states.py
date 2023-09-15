#!/usr/bin/python3
""" cript that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    tmp = sys.argv[4]
    db = MySQLdb.connect(
            host="localhost", user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY\
            '{}' ORDER BY id ASC".foramt(sys.argv[4]), tmp)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close() 