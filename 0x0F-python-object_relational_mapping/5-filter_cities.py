#!/usr/bin/python3
""" module filter state Db with safe from SQL injection """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ func not run when imported as module """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    query = "SELECT cities.name \
            FROM cities WHERE \
            cities.state_id = (SELECT states.id FROM states \
            WHERE states.name LIKE BINARY %s) ORDER BY cities.id"
    cur.execute(query, (argv[4],))
    rows = cur.fetchall()
    if len(rows) == 0:
         print()
    for i in range(len(rows)):
        print(rows[i][0], end="")
        if i == len(rows) - 1:
            print()
        else:
            print(end=", ")
    cur.close()
    db.close()
