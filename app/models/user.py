from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.session import Session
from models.qr_code import QRCode
from db import db

class User(db.Model):
  __tablename__ = 'users'
  
  id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
  email: Mapped[str] = mapped_column(db.String, unique=True, nullable=False)
  password: Mapped[str] = mapped_column(db.String, nullable=True)

  session: Mapped['Session'] = relationship(back_populates='user')
  qr_codes: Mapped[list['QRCode']] = relationship(back_populates='user')