from enum import Enum, auto

from enum import 
from pydantic import BaseModel, validator
from sqlalchemy import Column, Integer, Uuid, String

from service.database import Base


# Database Models
class User(Base):
    """User table"""

    __tablename__ = "users"

    id = Column(Uuid, primary_key=True, index=True)
    song_preference = Column(Integer)


class Song(Base):
    """Song table"""

    __tablename__ = "songs"

    id = Column(Uuid, primary_key=True, index=True)
    name = Column(String, index=True)
    categories = Column(Integer)


# SongCategory Mapping
class SongCategory(Enum):
    ELECTRONIC = 0
    JAZZ = 1
    HIP_HOP = 2
    FOLK = 3
    AFROBEAT = 4


# Pydantic Models
class UserPreferences(BaseModel):
    categories = list[SongCategory]

    @validator("categories", each_item=True)
    def validate_category(cls, v):
        """Validate song category"""
        if v.upper() not in SongCategory.__members__:
            raise ValueError(f"Invalid Category: {v}")
        return v.lower()
