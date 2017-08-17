#!/usr/bin/python3

''' listing all object in a table '''

if __name__== '__main__':

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
    argv[1], argv[2], argv[3]))
Base.metadata.create_all(engine)

Session.sessionmaker(bind=engine)
session = Session()

for state in session.query(State).filter(State.name.contains('a')):
    try:
        print("{}: {}".format(state.id, state.name))
    except:
        print("Nothing")
session.close()
