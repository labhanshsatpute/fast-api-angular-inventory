
from sqlalchemy import String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, ModelMixin


class UnitOfMeasure(ModelMixin, Base):
    __tablename__ = "units_of_measure"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )

    abbreviation: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        unique=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        index=True,
    )
