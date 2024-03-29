#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, select

if __name__ == "__main__":
    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                ),
                 pool_pre_ping=True,
                 )

    with engine.connect() as connection:
        query = select(State).order_by(State.id.asc())
        states = connection.execute(query).fetchone()
        if states:
<<<<<<< HEAD
            print(f"{state.id}: {state.name}")
=======
            print(f"{states.id}: {states.name}")
>>>>>>> 118d34f423ebc2c2b78bdf5ad3263e7418e74dc2
        else:
            print("Nothing")

    engine.dispose()
