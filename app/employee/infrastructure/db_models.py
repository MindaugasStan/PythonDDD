import datetime

from sqlalchemy import DateTime, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.company.infrastructure.db_models import Company
from app.core.base_db_model import BasePlusDateTime
from app.seniority_level.infrastructure.db_models import SeniorityLevel


class Employee(BasePlusDateTime):
    __tablename__ = "employees"  # Ensure table name is consistent

    employee_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    lastname: Mapped[str] = mapped_column(Text, nullable=False)
    email: Mapped[str] = mapped_column(Text, nullable=False)
    jobstartdate: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
    )
    jobenddate: Mapped[datetime.datetime] = mapped_column(
        DateTime(timezone=True),
    )
    hourlyrate: Mapped[float] = mapped_column()
    experience: Mapped[float] = mapped_column()

    # Fix: Ensure foreign keys reference the correct column
    company_id: Mapped[int] = mapped_column(
        ForeignKey(
            "companies.company_id", ondelete="RESTRICT"
        ),  # Corrected FK reference
    )
    employee_company: Mapped["Company"] = relationship(
        "Company",
        back_populates="employees",
        lazy="joined",
        cascade="all, delete-orphan",
    )

    senioritylevel_id: Mapped[int] = mapped_column(
        ForeignKey(
            "seniority_levels.seniority_level_id", ondelete="RESTRICT"
        ),  # Fixed FK reference
    )
    seniority_level: Mapped["SeniorityLevel"] = relationship(
        "SeniorityLevel",
        back_populates="employees",
        lazy="joined",
        cascade="all, delete-orphan",
    )
