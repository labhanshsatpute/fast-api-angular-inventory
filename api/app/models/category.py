import uuid

from sqlalchemy import String, Text, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base, ModelMixin


class Category(ModelMixin, Base):
    __tablename__ = "categories"

    name: Mapped[str] = mapped_column(
        String(100),
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

    parent_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("categories.id", ondelete="RESTRICT"),
        nullable=True,
        index=True,
    )

    status: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    parent: Mapped["Category | None"] = relationship(
        back_populates="children",
        remote_side="Category.id",
    )

    children: Mapped[list["Category"]] = relationship(
        back_populates="parent",
    )