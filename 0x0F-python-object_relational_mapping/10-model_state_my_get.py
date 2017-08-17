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

state_1 = session.query(State).filter(State.name == argv[4])
try:
    print("{}".format(state_1[0].id))
except:
    print("Not found")

