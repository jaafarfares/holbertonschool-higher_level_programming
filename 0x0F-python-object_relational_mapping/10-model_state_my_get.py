#!/usr/bin/python3
"""
the comment below is for the default implementation
"""


from sqlalchemy.orm import Session
import sqlalchemy
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)
    session = Session(engine)
    states = session.query(State).filter(State.name == argv[4]).first()
    """ point to the first row in thetable states"""
    if states is None:
        print("Not found")
    else:
        print("{}".format(states.id))
    session.close()
    """ finaly lets close the session """
