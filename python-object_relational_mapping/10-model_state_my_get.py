#!/usr/bin/python3
"""Script that prints the State object with the name matching the
argument passed to the script from the database hbtn_0e_6_usa.
Displays the state id if found, otherwise displays Not found.
Uses SQLAlchemy filter_by method to safely search by name."""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter_by(name=sys.argv[4]).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()

