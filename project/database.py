import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ['POSTGRES_USER']}:{os.environ['POSTGRES_PASSWORD']}@" \
                          f"{os.environ['POSTGRES_HOST']}/{os.environ['POSTGRES_DB']}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

db_session = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False
    )
)

Base = declarative_base()
Base.query = db_session.query_property()
