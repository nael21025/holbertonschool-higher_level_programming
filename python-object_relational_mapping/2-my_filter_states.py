#!/usr/bin/python3
"""Filters states by user input"""
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
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(name)
    cursor.execute(query)
    
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    db.close()
