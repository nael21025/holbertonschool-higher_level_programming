#!/usr/bin/python3
"""Script that takes a state name as argument and lists all cities
of that state from the database hbtn_0e_4_usa using MySQLdb.
Safe from SQL injection through parameterized queries.
Results are sorted in ascending order by cities id.
Displays cities as comma-separated values on a single line."""
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
        "SELECT cities.name FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],)
    )

    cities = [row[0] for row in cursor.fetchall()]
    print(", ".join(cities))

    cursor.close()
    db.close()

