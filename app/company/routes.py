# pylint: disable=unused-argument
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.company.application.dto import CreateCompanyDTO, ReadCompanyDTO
from app.company.application.services import CompanyCreator, CompanyFinder
from app.company.dependencies import company_creator, company_finder
from app.dependencies import get_db

company_router = APIRouter(
    prefix="/companies",
    tags=["Companies"],
)


@company_router.get(
    "/{key}",
    response_model=ReadCompanyDTO,
)
def get_company(
    key: int,
    service: CompanyFinder = Depends(company_finder),
):
    company = service.find_by_id(key)
    return company


@company_router.get("/", response_model=list[ReadCompanyDTO])
def get_companies(
    service: CompanyFinder = Depends(company_finder),
):
    companies = service.findall()
    return companies


@company_router.post(
    "/",
    response_model=ReadCompanyDTO,
    status_code=status.HTTP_201_CREATED,
)
def create_seniority_level(
    data: CreateCompanyDTO,
    service: CompanyCreator = Depends(company_creator),
    session: Session = Depends(get_db),
):
    print(data)
    company = service.create(create_company=data)

    session.commit()

    return company
