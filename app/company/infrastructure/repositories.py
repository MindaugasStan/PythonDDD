# pylint: disable=arguments-renamed
import logging

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.company.domain.aggregates import Company
from app.company.infrastructure.db_models import Company as DBCompany
from app.core.base_repository import BaseRepository

logger = logging.getLogger(__name__)


class CompanyRepository(BaseRepository):

    def __init__(self, session: Session):
        self._session: Session = session

    def find_by_id(self, id_: int) -> Company:
        db_model = self._session.get(DBCompany, id_)
        if not db_model:
            raise NoResultFound(f"Company with id[{id_}] cannot be found.")

        return self._to_entity(db_model)

    def findall(self) -> list[Company]:
        db_models = list(self._session.scalars(select(DBCompany)).all())
        return [self._to_entity(db_model) for db_model in db_models]

    def save(self, company: Company) -> None:
        # pylint: disable=protected-access
        db_model = self._from_entity(company)
        self.create(company, db_model)

    def create(self, company, db_model):
        # pylint: disable=protected-access
        logger.debug("Creating company")
        self._session.add(db_model)
        self._session.flush()
        self._session.refresh(db_model)
        company._updated_at = db_model.updated_at
        company._created_at = db_model.created_at
        company._company_id = db_model.company_id

    def update(self, company, db_model):
        db_model = self._session.merge(db_model)
        self._session.flush()
        self._session.refresh(db_model)
        # pylint: disable=protected-access
        company._updated_at = db_model.updated_at
        company._created_at = db_model.created_at

    def delete_by_id(self, id_: int):
        pass

    def _to_entity(self, db_model: DBCompany) -> Company:
        return Company(
            company_id=db_model.company_id,
            name=db_model.name,
            created_at=db_model.created_at,
            updated_at=db_model.updated_at,
        )

    def _from_entity(self, company: Company) -> DBCompany:
        snapshot = company.to_snapshot()
        snapshot.pop("created_at")
        snapshot.pop("updated_at")
        return DBCompany(**snapshot)
