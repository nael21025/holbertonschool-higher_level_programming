#!/usr/bin/python3
"""Module that defines the State class and creates a Base class
for declarative model definitions in SQLAlchemy ORM.
The State class is linked to the MySQL table states with auto-increment
primary key and name field with constraints."""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class that defines the State model and links to the MySQL
    table states. Contains id as primary key and name as varchar field.
    Both fields have appropriate constraints defined."""
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)

