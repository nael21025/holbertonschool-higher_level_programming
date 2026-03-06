#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the
states table where the name matches the argument, safe from SQL injection.
Uses parameterized queries with %s placeholder to prevent SQL injection.
Results are sorted in ascending order by state id."""
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
    cursor.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC",
        (sys.argv[4],)
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

