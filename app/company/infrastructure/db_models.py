from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.base_db_model import BasePlusDateTime


class Company(BasePlusDateTime):
    __tablename__ = "companies"
    company_id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)
    levels: Mapped["SeniorityLevel"] = relationship(
        lazy="joined", cascade="all, delete-orphan"
    )
    employees: Mapped["Employee"] = relationship(
        lazy="joined", cascade="all, delete-orphan"
    )
