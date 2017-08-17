#!/usr/bin/python3

''' listing all object in a table '''


import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__ == '__main__':
    host = "localhost"
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        user,
        password,
        host,
        port,
        databae))

    Session.sessionmaker(bind=engine)
    session = Session()

    state_1 = session.query(State.id, State.name).first()
    if (state_1 is None):
        print("{}: {}"/format(state_1.id, str(state_1)))
    else:
        print("Nothing")
    session.close()
