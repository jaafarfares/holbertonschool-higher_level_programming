#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(
        Integer,
        Unique=True,
        primary_key=True,
        null=True,
        autogenerated=True)
    name = Column(String(128))
