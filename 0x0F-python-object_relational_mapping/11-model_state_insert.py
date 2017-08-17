#!/usr/bin/python3

''' listing all object in a table '''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

if __name__== '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    Session.sessionmaker(bind=engine)
    session = Session()

    state_new = State(name="Louisiana")
    session.add(state_new)
    session.commit()
    print(state_new.id)
