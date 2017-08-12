#!/usr/bin/python3
"""selecting items from a db"""

if __name__ == "__main__":
        import MySQLdb
        import sys

        username = sys.argv[1]
        password = sys.argv[2]
        db = sys.argv[3]

        connect = MySQLdb.connect(user=username,
                                  host="localhost",
                                  port=3306,
                                  password=password,
                                  db=db)

        connection = connect.cursor()
        connection.execute("SELECT * FROM states WHERE name LIKE BINARY \
                'N%' ORDER BY id ASC")

        query_row = connection.fetchone()
        for row in query_row:
                print(query_row)
                query_row = connection.fetchone()
        connection.close()
        connect.close()
