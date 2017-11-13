#!/usr/bin/python3
"""Contains State class mapped to states table in the DB"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sys import argv
from model_city import State, City


if __name__ == "__main__":
    # set up connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))

    # binding ORM's handle to the database
    Session = sessionmaker(bind=engine)

    # set up connection to retrieve data from the DB
    session = Session()

    # list all city objects from the database
    for instance in session.query(City).order_by(City.id):
        print("{:s}: ({:d}) {:s}".format(
            instance.state.name, instance.id, instance.name))
