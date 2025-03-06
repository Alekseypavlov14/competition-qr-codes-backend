from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from db import db

class Session(db.Model):
  __tablename__ = 'sessions'

  id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
  token: Mapped[str] = mapped_column(db.String, nullable=False)

  user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
  user: Mapped['User'] = relationship(back_populates='session') 
