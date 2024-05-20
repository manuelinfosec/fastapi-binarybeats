import uuid
from typing import List

from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from sqlalchemy.orm import Session

from service.crud import get_matching_songs, get_user
from service.dependency import get_db
from service.helpers import decode_preferences, encode_preferences
from service.models import SongCategory, UserPreferences

router = APIRouter()


@router.get("/users/{user_id}/preferences")
def get_user_preferences(user_id: uuid.UUID, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Convert decimal to user preference by comparing bit-shifted values
    user_preferences: List[SongCategory] = decode_preferences(user.song_preference)
    return {"categories": [category.name for category in user_preferences]}


@router.post("/users/{user_id}/preferences")
def set_user_preferences(
    user_id: uuid.UUID, preferences: UserPreferences, db: Session = Depends(get_db)
):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Convert categories to decimal by bit-shifting
    user.song_preference = encode_preferences(preferences)
    db.commit()
    return {"message": "Preference updated successfully"}


@router.get("/users/{user_id}/matches")
def find_matches(user_id: uuid.UUID, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Get all matching song with bitwise AND for non-zero comparisons
    matching_songs = get_matching_songs(db, user)
    return {"matching_songs": [song.name for song in matching_songs]}
