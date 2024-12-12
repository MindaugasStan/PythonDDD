# pylint: disable=unused-argument
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependencies import get_db
from app.employee.application.dto import CreateEmployeeDTO, ReadEmployeeDTO
from app.employee.application.services import EmployeeCreator, EmployeeFinder
from app.employee.dependencies import employee_creator, employee_finder

employee_router = APIRouter(
    prefix="/employee",
    tags=["Employees"],
)


@employee_router.get(
    "/{key}",
    response_model=ReadEmployeeDTO,
)
def get_employee(
    key: int,
    service: EmployeeFinder = Depends(employee_finder),
):
    address = service.find_by_id(key)
    return address


@employee_router.get("/", response_model=list[ReadEmployeeDTO])
def get_employees(
    service: EmployeeFinder = Depends(employee_finder),
):
    employees = service.findall()
    return employees


@employee_router.post(
    "/",
    response_model=ReadEmployeeDTO,
    status_code=status.HTTP_201_CREATED,
)
def create_employee(
    data: CreateEmployeeDTO,
    service: EmployeeCreator = Depends(employee_creator),
    session: Session = Depends(get_db),
):
    employee = service.create(create_employee=data)
    session.commit()

    return employee
