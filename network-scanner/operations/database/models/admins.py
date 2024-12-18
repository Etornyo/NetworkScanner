from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Boolean, String
from pydantic import EmailStr
# from datetime import datetime

from ScanNet.operations.database.core import Base



class Admin(Base):
    __tablename__="admin"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column (String, nullable=False)
    email: Mapped[EmailStr] = mapped_column (String, unique=True, nullable=False)
    is_active: Mapped[bool] = mapped_column (Boolean, default=True)