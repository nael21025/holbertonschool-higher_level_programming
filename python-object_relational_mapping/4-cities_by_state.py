#!/usr/bin/python3
"""
4-cities_by_state.py
Script that lists all cities from the database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    """
    Main function to connect to the database,
    And retrieve all the cities.
    """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    cursor = db.cursor()

    query = (
        "SELECT cities.id, cities.name, states.name FROM cities "
        "JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC"
    )
    cursor.execute(query)
    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    db.close()
#!/usr/bin/python3
"""
4-cities_by_state.py

Displays all cities with their corresponding state names
"""
import MySQLdb
import sys


if __name__ == "__main__":
    """
    Main function that executes the database
    connection and displays cities with states.
    """

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
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

