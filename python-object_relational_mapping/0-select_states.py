#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
using MySQLdb module to fetch and display all state records
Ordered by state id in ascending order."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

