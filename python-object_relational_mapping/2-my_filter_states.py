#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where the name matches the argument.
Uses format string to build the SQL query with user input.
Results are sorted in ascending order by state id."""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        host="localhost",
        charset="utf8mb4"
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

