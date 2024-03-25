import MySQLdb

def list_states(username, password, database_name):
    """
    Connects to the specified MySQL database and lists states sorted by ID.
    """

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database_name
        )
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error:", e)

    finally:
        if db:
            db.close()
