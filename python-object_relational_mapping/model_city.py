#!/usr/bin/python3
"""
model_city.py
Defines the City class which maps to the cities table in the database.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

# ...existing code...
#!/usr/bin/python3
"""Module that defines the City class for SQLAlchemy ORM model.
The City class is linked to the MySQL table cities and has a
foreign key relationship to the State class through state_id."""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """Class that defines the City model and links to the MySQL table
    cities. Contains id as primary key, state_id as foreign key to states,
    and name field. All fields have appropriate constraints."""
    __tablename__ = 'cities'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    state_id = Column(
        Integer,
        ForeignKey('states.id'),
        nullable=False
    )
    name = Column(String(128), nullable=False)

