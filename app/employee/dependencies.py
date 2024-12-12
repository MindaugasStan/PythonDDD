from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.employee.application.services import EmployeeCreator, EmployeeFinder
from app.employee.infrastructure.repositories import EmployeeRepository


def employee_repository(
    session: Session = Depends(get_db),
) -> EmployeeRepository:
    return EmployeeRepository(session)


def employee_finder(
    repository: EmployeeRepository = Depends(employee_repository),
) -> EmployeeFinder:
    return EmployeeFinder(repository)


def employee_creator(
    repository: EmployeeRepository = Depends(employee_repository),
) -> EmployeeCreator:
    return EmployeeCreator(repository)
