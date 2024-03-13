import enum
from sqlalchemy import Table, Column, MetaData, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.models.base import Base
from src.utils import get_public_id


class UserRoles(enum.Enum):
    EMPLOYEE = "EMPLOYEE"
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"


class User(Base):
    public_id: Mapped[str] = mapped_column(String(50), unique=True, nullable=False, default=get_public_id())
    username: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    role: Mapped[str] = mapped_column(Enum(UserRoles), default=UserRoles.EMPLOYEE, nullable=False)
