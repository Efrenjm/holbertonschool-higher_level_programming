#!/usr/bin/python3
"""
State class
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ Inherits from Base Tips and links to the MySQL table states """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
