#!/usr/bin/python3
"""
Write a python file that contains the class definition
of a State and an instance Base = declarative_base():
"""


import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ the class state imports Base"""

    __tablename__ = 'states'
    id = Column(
        Integer,
        nullable=False,
        primary_key=True,
        autoincrement=True,
        unique=True)
    name = Column(String(128), nullable=False)
