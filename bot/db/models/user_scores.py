from uuid import UUID

from sqlalchemy import BigInteger, ForeignKey, Integer, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.db import Base
from bot.db.models.mixins import TimestampMixin


class Score(TimestampMixin, Base):
    __tablename__ = 'scores'
    
    id: Mapped[UUID] = mapped_column(
        Uuid,
        primary_key=True,
        server_default=text("gen_random_uuid()")
    )   
    user_id: Mapped[int] = mapped_column(
        BigInteger,
        ForeignKey('users.telegram_id', ondelete='CASCADE')
    )
    number: Mapped[int] = mapped_column(Integer, nullable=False)
    
    user: Mapped["User"] = relationship(back_populates='scores')  # noqa: F821
