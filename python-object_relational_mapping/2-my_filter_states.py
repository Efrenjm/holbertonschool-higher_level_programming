#!/usr/bin/python3
"""
List all states in hbtn_0e_0_usa with a name
starting with a state name parameter
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name,
        charset="utf8"
    )
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM states WHERE name LIKE BINARY '{state_name}'")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()
