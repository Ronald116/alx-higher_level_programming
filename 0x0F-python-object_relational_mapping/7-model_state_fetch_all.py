#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """Connect to database"""
    
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                      argv[2], argv[3])
    
    engine = create_engine(url, echo=True)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    for list_states in session.query(State).order_by(State.id):
        print('{}: {}'.format(list_states.id, list_states.name))
