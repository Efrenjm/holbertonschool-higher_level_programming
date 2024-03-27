#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the db: hbtn_0e_6_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    mysql_usr = argv[1]
    mysql_pswd = argv[2]
    db_name = argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(mysql_usr, mysql_pswd, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    my_states = session.query(State).order_by(State.id).all()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    state = session.query(State).filter(State.name == 'Louisiana').first()
    print(state.id)
    session.close()