#!/usr/bin/python3

''' listing all object in a table '''

if __name__ == '__main__':

    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy import Column, Integer, String
    from sqlalchemy.orm import sessionmaker

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        user, password, host, port, database))

    session = sessionmaker(bind=engine)
    session = Session()
    for state in states:
        print("{}: {}".format(state, id, state.name))
session.close()
