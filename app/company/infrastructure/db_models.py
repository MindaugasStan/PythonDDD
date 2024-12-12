from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.base_db_model import BasePlusDateTime


class Company(BasePlusDateTime):
    __tablename__ = "companies"  # Ensure table name is consistent

    company_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)

    # Correct relationships for levels and employees
    levels: Mapped["SeniorityLevel"] = relationship(
        "SeniorityLevel",
        back_populates="company",
        lazy="joined",
        cascade="all, delete-orphan",
    )
    employees: Mapped["Employee"] = relationship(
        "Employee",
        back_populates="employee_company",
        lazy="joined",
        cascade="all, delete-orphan",
    )
