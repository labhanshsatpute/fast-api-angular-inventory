
from sqlalchemy import String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base, ModelMixin


class Brand(ModelMixin, Base):
    __tablename__ = "brands"

    name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
        index=True,
    )

    code: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
        unique=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    website: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    logo_url: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    status: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        index=True,
    )
