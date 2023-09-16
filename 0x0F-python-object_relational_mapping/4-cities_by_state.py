#!/usr/bin/python3
""" module filter state Db with safe from SQL injection """
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """ func not run when imported as module """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                         passwd=argv[2], db=argv[3])
    cur i= db.cursor()
    query = """SELECT cities.id, cities.name, states.name
    FROM cities INNER JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id""")
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
