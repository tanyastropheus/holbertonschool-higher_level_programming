#!/usr/bin/python3
"""Contains State class mapped to states table in the DB"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sys import argv

# allow to create mapping to the database
Base = declarative_base()


class State(Base):
    """connect State objects with the table 'states' in the DB, or
    create the table if it doesn't already exist in the DB"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # set up connection to the database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(argv[1], argv[2], argv[3]))

    # binding ORM's handle to the database
    Session = sessionmaker(bind=engine)

    # set up connection to retrieve data from the DB
    session = Session()

    # update a data entry to the table
    session.query(State).filter(State.id == 2).update({"name": "New Mexico"})

    # commit the change to the database
    session.commit()
