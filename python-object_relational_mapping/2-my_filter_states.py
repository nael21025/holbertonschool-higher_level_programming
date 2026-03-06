#!/usr/bin/python3
"""This module displays all values in the states table of hbtn_0e_0_usa where the name matches the argument provided by the user."""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()
    query = (
        "SELECT * FROM states WHERE name LIKE BINARY %s "
        "ORDER BY states.id ASC"
    )
    cursor.execute(query, (state_name,))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()