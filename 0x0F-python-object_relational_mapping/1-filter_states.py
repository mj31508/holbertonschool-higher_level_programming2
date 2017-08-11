#!/usr/bin/python3
"""selecting items from a db"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    connect = MySQLdb.connect(user=sys.argv[1], host="localhost",
                              port=3306, password=sys.argv[2],
                              db=sys.argv[3])

    now = connect.cursor()

    query_rows = now.fetchone()

    for row in query_rows:
        print(query_rows)
        query_rows = now.fetchone()
    now.close()
    connect.close()
