from fastapi import Depends
from sqlalchemy.orm import Session

from app.company.dependencies import company_repository
from app.company.infrastructure.repositories import CompanyRepository
from app.dependencies import get_db
from app.employee.application.services import EmployeeCreator, EmployeeFinder
from app.employee.infrastructure.repositories import EmployeeRepository
from app.seniority_level.dependencies import seniority_level_repository
from app.seniority_level.infrastructure.repositories import (
    SeniorityLevelRepository,
)


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
    company_repo: CompanyRepository = Depends(company_repository),
    seniority_level_repo: SeniorityLevelRepository = Depends(
        seniority_level_repository
    ),
) -> EmployeeCreator:
    return EmployeeCreator(repository, company_repo, seniority_level_repo)
