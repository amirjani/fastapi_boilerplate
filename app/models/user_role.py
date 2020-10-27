from sqlalchemy import Column, ForeignKey

from app.db.base_class import Base


class UserRole(Base):
    __tablename__ = 'user_role'

    user_id = Column('user_id', ForeignKey('user.id'), primary_key=True)
    role_id = Column('role_id', ForeignKey('role.id'), primary_key=True)
