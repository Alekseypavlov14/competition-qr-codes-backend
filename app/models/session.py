from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from models.user import User
from db import db

class Session(db.Model):
  __tablename__ = 'sessions'

  id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
  user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='CASCADE'))
  token: Mapped[str] = mapped_column(db.String)

  user: Mapped['User'] = relationship('User', back_populates='session') 
