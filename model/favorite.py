from sqlalchemy import Text, Column, ForeignKey
from sqlalchemy.orm import relationship

from model.base import Base


class Favorite(Base):
    __tablename__ = 'favorite'

    id = Column(Text, primary_key=True)
    song_id = Column(Text, ForeignKey('songs.id'))
    user_id = Column(Text, ForeignKey('users.id'))

    song = relationship('Song')
    user = relationship('User', back_populates='favorites')
