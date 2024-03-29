#!/usr/bin/python3
"""
List all cities with state name in hbtn_0e_4_usa with a name
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name,
        charset="utf8"
    )
    cursor = conn.cursor()

    query = "SELECT cities.id, cities.name, states.name\
            FROM cities JOIN states ON states.id = cities.state_id\
            ORDER BY cities.id ASC"

    cursor.execute(query)
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()
