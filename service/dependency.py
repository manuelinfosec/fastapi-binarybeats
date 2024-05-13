from sqlalchemy.orm import Session

from service.main import app


def get_db():
    """Get a database connection"""
    db: Session = app.state.db()
    try:
        yield db
    finally:
        db.close()
