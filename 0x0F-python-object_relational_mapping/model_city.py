#!/usr/bin/python3
'''Create the 'cities' table and the mapping to it'''

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)


class City(Base):
    '''link to cities table in MySQL'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    # reference to the state the specified city belongs to
    # "cities" referes to State.cities
    # back_populates establishes the type of relationships (one-to-many, etc.)
    state = relationship("State", back_populates="cities")

# reference to the cities in a specified state, ordered by city id
# "state" refers to the above state attribute
State.cities = relationship("City", order_by=City.id, back_populates="state")
