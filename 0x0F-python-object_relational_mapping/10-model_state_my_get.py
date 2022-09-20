#!/usr/bin/python3

"""
Print the state object id
"""

import sys
from model_state import Base, State

from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True,
    )
    Base.metadata.create_all(engine)

    session = Session(engine)
    found = False
    for state in (
        session.query(State).filter(State.name == sys.argv[4]).
        order_by(State.id)
    ):
        if state:
            print(f"{state.id}")
            found = True
            break
    if not found:
        print("Not found")
    session.close()
