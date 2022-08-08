#!/usr/bin/python3
"""
the comment below is for the default implementation
"""


from sqlalchemy.orm import Session
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, update

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    stmt = session.query(State).filter(State.id == 2).first()
    stmt.name = "New Mexico"
    session.add(stmt)
    session.commit()
    session.close()
    """ finaly lets close the session """
