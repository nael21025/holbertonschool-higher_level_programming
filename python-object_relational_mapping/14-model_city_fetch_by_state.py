#!/usr/bin/python3
"""Script that displays all cities from the database hbtn_0e_14_usa
with their corresponding state using SQLAlchemy ORM.
Performs a join between City and State tables and displays each as
state_name: (city_id) city_name ordered by city id."""
import sys
from model_state import Base, State
from model_city import City
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

    for city, state in session.query(City, State).join(
        State
    ).order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

