#!/usr/bin/python3
"""Filters and displays states by name from hbtn_0e_0_usa using parameterized queries."""
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
    name = sys.argv[4]
    cursor.execute(
        "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(name)
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

