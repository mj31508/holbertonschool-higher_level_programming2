#!/usr/bin/python3
"""selecting items from a db"""

if __name__ == "__main__":
        import MySQLdb
        import sys

        username = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]
        state = sys.argv[4]

        connect = MySQLdb.connect(user=username,
                                  host="localhost",
                                  port=3306,
                                  password=password,
                                  db=db)

        connection = connect.cursor()
        connection.execute("SELECT * FROM states WHERE name LIKE BINARY \
                %s ORDER BY id ASC", (state, ))

        state = connection.fetchone()
        while state:
                print(state)
                state = connection.fetchone()
        connection.close()
        connect.close()
