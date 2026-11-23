import uuid
from sqlalchemy import String, Boolean, Text, ForeignKey, Numeric, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.base import Base, ModelMixin
from decimal import Decimal

class ProductVariant(ModelMixin, Base):
    __tablename__  = "product_variants"

    product_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    variant_name: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True
    )

    sku: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True,
        index=True
    )

    barcode: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
        unique=True,
    )

    unit_of_measure_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("units_of_measure.id", ondelete="RESTRICT"),
        nullable=False,
        index=True
    )

    attributes: Mapped[dict[str, str] | None] = mapped_column(
        JSON,
        nullable=True
    )

    purchase_price: Mapped[Decimal] = mapped_column(
        Numeric(14,2),
        default=Decimal("0.00"),
        nullable=False
    )

    selling_price: Mapped[Decimal] = mapped_column(
        Numeric(14,2),
        default=Decimal("0.00"),
        nullable=False
    )

    is_default: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False
    )

    status: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
        index=True
    )

    product: Mapped["Product"] = relationship(
        back_populates="variants"
    )

    unit_of_measure: Mapped["UnitOfMeasure"] = relationship()