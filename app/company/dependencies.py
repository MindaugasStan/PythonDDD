from fastapi import Depends
from sqlalchemy.orm import Session

from app.company.application.services import CompanyCreator, CompanyFinder
from app.company.infrastructure.repositories import CompanyRepository
from app.dependencies import get_db


def company_repository(
    session: Session = Depends(get_db),
) -> CompanyRepository:
    return CompanyRepository(session)


def company_finder(
    repository: CompanyRepository = Depends(company_repository),
) -> CompanyFinder:
    return CompanyFinder(repository)


def company_creator(
    repository: CompanyRepository = Depends(company_repository),
) -> CompanyCreator:
    return CompanyCreator(repository)
