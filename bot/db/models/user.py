from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bot.db import Base
from bot.db.models.mixins import TimestampMixin

class User(TimestampMixin, Base):
    __tablename__ = 'users'
    
    telegram_id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str] = mapped_column(String, nullable=False)
    last_name: Mapped[str] = mapped_column(String, nullable=True)
    
    scores: Mapped[list["Score"]] = relationship(back_populates="user")  # noqa: F821