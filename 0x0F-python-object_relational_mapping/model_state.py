#!/usr/bin/python3
"""model state
"""
from sqlalchemy import Column, Integer, String, ForrignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

Base = declarative_base()

class City(Base):
    """ class definition """
        __tablename__ = 'cities'
            id = Column(Integer, primary_key=True)
            name =  Column(String(50))
            state_id = Column(Integer, ForeignKey('states.id'))
