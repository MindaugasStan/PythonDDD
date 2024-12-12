import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from app.configs import Database

logger = logging.getLogger(__name__)


def get_db():
    engine = create_engine(Database().postgres_dsn)
    session_local = sessionmaker(
        autocommit=False, autoflush=False, bind=engine
    )
    logger.debug("Creating database session")
    try:
        db = session_local()
        yield db
    finally:
        logger.debug("Closing database session")
        db.close()


Base = declarative_base()
