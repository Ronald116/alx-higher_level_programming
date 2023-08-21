#!/usr/bin/python3
"""
a script that prints the first State object from the database hbtn_0e_6_usa
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sys import argv

if __name__ == "__main__":
    """connect to database and access first state"""
    
    url = "mysql+mysqldb://{}:{}@localhost/{}".format(argv[1],
                                                      argv[2], argv[3])
    
    engine = create_engine(url)
    Session = sessionmaker(bind=engine)
    session = Session()
    
    first_state = session.query(State).order_by(State.id).first()
    
    if first_state is not None:
        print('{}: {}'.format(first_state.id, first_state.name))
    else:
        print('Nothing')
