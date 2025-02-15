from sqlalchemy import INTEGER, String
from sqlalchemy.orm import mapped_column, Mapped

from .base import Base


class Group(Base):
    __tablename__ = 'groups'
    id: Mapped[int] = mapped_column(INTEGER, primary_key=True)
    url: Mapped[str] = mapped_column(String)
    sub_count: Mapped[int] = mapped_column(INTEGER)
    key_word: Mapped[str] = mapped_column(String)
