# This is for defining the database to be used.
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
# from pymongo import MongoClient

# SQL database for product
engine = create_engine(
    "sqlite:///networkscan.sqlite",
    echo=True,
    connect_args={"check_same_thread": False, })

SessionMaker = sessionmaker(
    bind=engine,
    autoflush=False,
    expire_on_commit=False,
    autocommit=False
)


class Base(DeclarativeBase):
    pass