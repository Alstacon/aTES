from sqlalchemy import Table, Column, MetaData, Enum, Integer, String, TIMESTAMP, ForeignKey

from services.auth.src.utils import get_public_id

meta_data = MetaData()


class UserRoles(Enum):
    EMPLOYEE = "EMPLOYEE"
    ADMIN = "ADMIN"
    MANAGER = "MANAGER"


class User:
    __table__ = Table(
        'user',
        meta_data,
        Column('id', Integer, primary_key=True),
        Column(
            'public_id',
            String(50),
            unique=True,
            default=get_public_id,
            nullable=False
        ),
        Column('username', String(50), nullable=False),
        Column('email', String(50), nullable=False, unique=True),
        Column('role',
               Enum(UserRoles),
               default=UserRoles.EMPLOYEE,
               nullable=False)
    )

    id: int
    public_id: str
    username: str
    email: str
    role: UserRoles
