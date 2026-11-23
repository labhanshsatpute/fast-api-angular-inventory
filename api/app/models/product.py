from sqlalchemy import String, Boolean, ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base, ModelMixin
import uuid

class Product(ModelMixin, Base):
    __tablename__ = "products"

    name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    category_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("categories.id", ondelete="RESTRICT"),
        nullable=True,
        index=True
    )

    brand_id: Mapped[uuid.UUID | None] = mapped_column(
        ForeignKey("brands.id", ondelete="RESTRICT"),
        nullable=True,
        index=True
    )

    track_inventory: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        index=True
    )

    status: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        index=True,
        nullable=False
    )

    category: Mapped["Category | None"] = relationship()
    brand: Mapped["Brand | None"] = relationship()

    variants: Mapped[list["ProductVariant"]] = relationship(
        back_populates="product",
        cascade="all, delete-orphan"
    )

