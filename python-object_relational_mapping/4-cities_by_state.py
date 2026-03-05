#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa
using only one execute() call to join cities with their corresponding states.
Results are sorted in ascending order by cities id.
Displays each city as: (id, name, state_name)."""
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
    cursor.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

