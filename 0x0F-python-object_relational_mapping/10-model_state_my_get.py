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

    # print state.id corresponding to the specified state.name from commandline
    # can also use one(), but need to catch the raised exception
    result = session.query(State.id).filter_by(name=argv[4]).first()

    if result is None:
        print("Not found")
    else:
        print(result[0])
