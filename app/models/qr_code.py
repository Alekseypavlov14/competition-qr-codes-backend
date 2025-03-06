from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from models.scan import Scan
from db import db

class QRCode(db.Model):
  __tablename__ = 'qr_codes'
  
  id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
  hash: Mapped[str] = mapped_column(db.String, unique=True)

  user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
  user: Mapped['User'] = relationship(back_populates='qr_codes')

  scans: Mapped[list['Scan']] = relationship(back_populates='qr_code')
