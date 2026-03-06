#!/usr/bin/python3
"""
model_state.py
python file that contains the class definition of a State,
And an instance Base = declarative_base().
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# ...existing code...
#!/usr/bin/python3
"""
model_state.py

Defines the State class for SQLAlchemy ORM
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class that defines the State model and links to the MySQL
    table states. Contains id as primary key and name as varchar field.
    Both fields have appropriate constraints defined.
    """
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
    )
    name = Column(String(128), nullable=False)

