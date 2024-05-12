import os

from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class User(Base):
    """User table"""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    song_preference = Column(Integer)


class Song(Base):
    """Song table"""

    __tablename__ = "songs"

    id = Column(Integer, primary_key=True, index=True)
    categories = Column(Integer)


def setup_database(app):
    pass
