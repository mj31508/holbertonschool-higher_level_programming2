#!/usr/bin/python3
"""selecting items from a db"""

if __name__ == "__main__":
        import MySQLdb
        import sys

        username = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]
        state = sys.argv[4]

        db_connect = MySQLdb.connect(user=username,
                                  host="localhost",
                                  port=3306,
                                  password=password,
                                  db=db)

        connection = db_connect.cursor()
        connection.execute("SELECT cities.id, cities.name, states.name \
        FROM cities \
        JOIN states ON cities.stateid = states.id \
        ORDER BY cities.id ASC")

        state = connection.fetchone()
        while (city):
                print(city)
                city = connection.fetchone()
