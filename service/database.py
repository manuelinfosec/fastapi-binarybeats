"""Database operations"""

import os

from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = os.environ["DATABASE_URL"]

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def setup_database(app: FastAPI):
    """Establish or dispose database connection"""

    @app.on_event("startup")
    async def startup_db():
        try:
            app.state.db = SessionLocal
            app.state.db().execute("SELECT 1")
        except OperationalError as err:
            raise RuntimeError("No connection to database") from err
