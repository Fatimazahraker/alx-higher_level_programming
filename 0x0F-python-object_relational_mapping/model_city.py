#!/usr/bin/python3
"""model state
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()

class City(Base):
    """ class definition """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name =  Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
