#!/usr/bin/python3
"""selecting items from a db"""

if __name__ == "__main__":
        import MySQLdb
        import sys

        username = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]

        db_connect = MySQLdb.connect(user=username,
                                     xhost="localhost",
                                     port=3306,
                                     password=password,
                                     db=db)

        connection = db_connect.cursor()
        connection.execute("SELECT cities.id, cities.name, states.name \
        FROM cities \
        JOIN states ON cities.state_id = states.id \
        ORDER BY cities.id ASC")

        city = connection.fetchone()
        while (city):
                print(city)
                city = connection.fetchone()
