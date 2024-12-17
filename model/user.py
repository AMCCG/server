from sqlalchemy import Column, TEXT, VARCHAR, LargeBinary
from sqlalchemy.orm import relationship

from model.base import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(TEXT, primary_key=True)
    name = Column(VARCHAR(100))
    email = Column(VARCHAR(100))
    password = Column(LargeBinary)
    favorites = relationship('Favorite', back_populates='user')
