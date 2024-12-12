from __future__ import annotations

import datetime

from sqlalchemy import DateTime, MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.sql import func


class _BaseDeclarative(DeclarativeBase):
    metadata = MetaData(
        naming_convention={
            "ix": "ix_%(column_0_label)s",
            "uq": "uq_%(table_name)s_%(column_0_name)s",
            "ck": "ck_%(table_name)s_%(constraint_name)s",
            "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
            "pk": "pk_%(table_name)s",
        }
    )
    type_annotation_map = {
        datetime.datetime: DateTime(timezone=True),
    }

    def __repr__(self):
        package = self.__class__.__module__
        class_name = self.__class__.__name__
        attrs = ", ".join(
            f"{key}={getattr(self, key)!r}"
            for key in sorted(self.__mapper__.columns.keys())
        )
        return f"{package}.{class_name}({attrs})"


class BasePlusDateTime(_BaseDeclarative):
    __abstract__ = True
    created_at: Mapped[datetime.datetime] = mapped_column(
        # pylint: disable=not-callable
        DateTime(timezone=True),
        server_default=func.now(),
        sort_order=100,
    )
    updated_at: Mapped[datetime.datetime] = mapped_column(
        # pylint: disable=not-callable
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.current_timestamp(),
        sort_order=102,
    )
