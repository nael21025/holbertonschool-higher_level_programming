#!/usr/bin/python3
"""Safely filters states from user input - prevents SQL injection"""
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
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id ASC", (name,))
    
    for row in cursor.fetchall():
        print(row)
    
    cursor.close()
    db.close()
