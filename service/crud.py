"""Database CRUD functions"""

import uuid
from typing import Optional, List

from sqlalchemy.orm import Session

from service.models import User, Song


def get_user(db: Session, user_id: uuid.UUID) -> Optional[User]:
    """
    Retrieve a user from the database by user ID.

    Args:
        db (Session): Database session.
        user_id (uuid.UUID): Unique identifier of the user.

    Returns:
        Optional[User]: The user object if found, otherwise None.
    """
    return db.query(User).get(user_id)


def get_matching_songs(db: Session, user: User) -> List[Song]:
    """
    Retrieve songs that match the user's preferences.

    Parameters:
        - db (Session): The database session.
        - user (User): The user object whose preferences will be used for matching.

    Returns:
        - List[Song]: A list of songs that match the user's preferences.

    Description:
        This function queries the database to retrieve songs that match the user's preferences.
        It performs a bitwise operation between the categories of each song and the user's
        song_preference attribute to determine if there is a match. If the result of the bitwise
        operation is non-zero, it indicates a match between the user's preferences and the song's
        categories. The function returns a list of all matching songs found in the database.
    """
    return db.query(Song).filter((Song.categories & user.song_preference) != 0).all()
