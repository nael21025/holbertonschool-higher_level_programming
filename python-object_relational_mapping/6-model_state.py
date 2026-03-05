#!/usr/bin/python3
"""Script that creates the State table in the database hbtn_0e_6_usa
using SQLAlchemy ORM. Creates all metadata tables defined in the models
through the Base.metadata.create_all() method with the database engine."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

