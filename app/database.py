"""DATABASE Connection"""

import os

from sqlmodel import SQLModel, Session, create_engine

POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_NAME = os.environ["POSTGRES_NAME"]
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
POSTGRES_HOST = os.environ["POSTGRES_HOST"]

CONNECTION_STRING = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:5432/{POSTGRES_NAME}"
print(CONNECTION_STRING)

engine = create_engine(CONNECTION_STRING)

SQLModel.metadata.create_all(engine)


def get_session():
    """Yields a session object for a database transaction"""
    with Session(engine) as session:
        yield session
