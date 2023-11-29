from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base


class Role(Base):
    __tablename__ = 'roles'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(length=50), nullable=False)
    permissions = Column(String(255))  # Здесь указывается длина для столбца permissions


    # Опционально: указание отношения один-ко-многим
    users = relationship("User", back_populates="role")

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=50), nullable=False)
    hashed_password = Column(String(length=255), nullable=False)
    role_id = Column(Integer, ForeignKey('roles.id'))

    # Опционально: указание отношения многие-к-одному
    role = relationship("Role", back_populates="users")

    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(
        TIMESTAMP, server_default=func.now(), onupdate=func.current_timestamp()
    )
