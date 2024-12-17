# pylint: disable=arguments-renamed
import logging

from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from app.core.base_repository import BaseRepository
from app.employee.domain.aggregates import Employee
from app.employee.infrastructure.db_models import Employee as DBEmployee

logger = logging.getLogger(__name__)


class EmployeeRepository(BaseRepository):

    def __init__(self, session: Session):
        self._session: Session = session

    def find_by_id(self, id_: int) -> Employee:
        db_model = self._session.get(DBEmployee, id_)
        if not db_model:
            raise NoResultFound(f"Employee with id[{id_}] cannot be found.")

        return db_model

    def findall(self) -> list[Employee]:
        db_models = list(self._session.scalars(select(DBEmployee)).all())
        return [self._to_entity(db_model) for db_model in db_models]

    def save(self, employee: Employee) -> None:
        # pylint: disable=protected-access
        db_model = self._from_entity(employee)
        self.create(employee, db_model)

    def create(self, employee, db_model):
        # pylint: disable=protected-access
        logger.debug("Creating Employee")
        self._session.add(db_model)
        self._session.flush()
        self._session.refresh(db_model)
        employee._updated_at = db_model.updated_at
        employee._created_at = db_model.created_at
        employee._employee_id = db_model.employee_id

    def update(self, employee, db_model):
        db_model = self._session.merge(db_model)
        self._session.flush()
        self._session.refresh(db_model)
        # pylint: disable=protected-access
        employee._updated_at = db_model.updated_at
        employee._created_at = db_model.created_at

    def delete_by_id(self, id_: int):
        pass

    def _to_entity(self, db_model: DBEmployee) -> Employee:
        return Employee(
            name=db_model.name,
            lastname=db_model.lastname,
            jobstartdate=db_model.jobstartdate,
            jobenddate=db_model.jobenddate,
            hourlyrate=db_model.hourlyrate,
            experience=db_model.experience,
            company_id=db_model.company_id,
            created_at=db_model.created_at,
            updated_at=db_model.updated_at,
            email=db_model.email,
        )

    def _from_entity(self, employee: Employee) -> DBEmployee:
        snapshot = employee.to_snapshot()
        snapshot.pop("created_at")
        snapshot.pop("updated_at")
        return DBEmployee(**snapshot)
