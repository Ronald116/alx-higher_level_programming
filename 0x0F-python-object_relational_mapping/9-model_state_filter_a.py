#!/usr/bin/python3
"""
a script that lists all State objects that contain
the letter a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    """connect to database and access states that contain letter 'a'"""
    
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                      argv[2], argv[3])
    
    engine = create_engine(url)
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    states = session.query(State).filter(State.name.like('%a%')).all()
    
    for state in states:
        print('{}: {}'.format(state.id, state.name))
    
