from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime, timezone
from sqlalchemy import Uuid, DateTime
from uuid import uuid4

class Base(DeclarativeBase):
    id: Mapped = mapped_column(
        Uuid(as_uuid=True),
        primary_key=True,
        default=uuid4
    )

    created_at: Mapped = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False
    )