# pylint: disable=arguments-renamed
import logging

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.core.base_repository import BaseRepository
from app.seniority_level.domain.aggregates import SeniorityLevel
from app.seniority_level.infrastructure.db_models import (
    SeniorityLevel as DBSeniorityLevel,
)

logger = logging.getLogger(__name__)


class SeniorityLevelRepository(BaseRepository):

    def __init__(self, session: Session):
        self._session: Session = session

    def find_by_id(self, id_: int) -> SeniorityLevel:
        db_model = self._session.get(DBSeniorityLevel, id_)
        if not db_model:
            raise NoResultFound(
                f"Seniority Level with id[{id_}] cannot be found."
            )

        return self._to_entity(db_model)

    def findall(self) -> list[SeniorityLevel]:
        db_models = list(self._session.scalars(select(DBSeniorityLevel)).all())
        return [self._to_entity(db_model) for db_model in db_models]

    def save(self, seniority_level: SeniorityLevel) -> None:
        # pylint: disable=protected-access
        db_model = self._from_entity(seniority_level)
        self.create(seniority_level, db_model)

    def create(self, seniority_level, db_model):
        # pylint: disable=protected-access
        logger.debug("Creating Seniority Level")
        self._session.add(db_model)
        self._session.flush()
        self._session.refresh(db_model)
        seniority_level._updated_at = db_model.updated_at
        seniority_level._created_at = db_model.created_at
        seniority_level._seniority_level_id = db_model.seniority_level_id

    def update(self, seniority_level, db_model):
        db_model = self._session.merge(db_model)
        self._session.flush()
        self._session.refresh(db_model)
        # pylint: disable=protected-access
        seniority_level._updated_at = db_model.updated_at
        seniority_level._created_at = db_model.created_at

    def delete_by_id(self, id_: int):
        pass

    def _to_entity(self, db_model: DBSeniorityLevel) -> SeniorityLevel:
        return SeniorityLevel(
            seniority_level_id=db_model.seniority_level_id,
            levelname=db_model.levelname,
            multiplier=db_model.multiplier,
            time_needed=db_model.time_needed,
            company_id=db_model.company_id,
            created_at=db_model.created_at,
            updated_at=db_model.updated_at,
        )

    def _from_entity(
        self, seniority_level: SeniorityLevel
    ) -> DBSeniorityLevel:
        snapshot = seniority_level.to_snapshot()
        snapshot.pop("created_at")
        snapshot.pop("updated_at")
        return DBSeniorityLevel(**snapshot)
