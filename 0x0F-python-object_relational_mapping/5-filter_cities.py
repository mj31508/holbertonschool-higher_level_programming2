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
        connection.execute("SELECT name \
        FROM cities \
        WHERE stateid IN \
        (SELECT id FROM states \
        WHERE name LIKE \
        '{:s}')".format(state)

        cities = connection.fetchone()
        print(", ".join(city[0] for city in cities))
