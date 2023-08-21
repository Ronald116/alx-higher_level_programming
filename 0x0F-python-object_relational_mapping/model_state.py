#!/usr/bin/python3
"""
A python file that contains the class definition of a State
and an instance Base = declarative_base()
"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column
    
Base = declarative_base()
    
class State(Base):
    """a class State"""
    __tablename__ = "states"
        
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
