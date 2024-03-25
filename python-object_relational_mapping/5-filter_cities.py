#!/Users/efrenjimenez/Cursos/Holberton/holbieEnv/bin/python3
# !/usr/bin/python3
"""
List all cities with state name in hbtn_0e_4_usa with a name
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

    cursor.execute("SELECT cities.name\
            FROM cities JOIN states ON states.id = cities.state_id\
            WHERE states.name = %s", (state_name,))
    states = cursor.fetchall()

    for i, state in enumerate(states):
        if i < len(states)-1:
            print(state[0], end=", ")
        else:
            print(state[0])

    cursor.close()
    conn.close()
