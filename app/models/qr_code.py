from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.user import User
from models.scan import Scan
from db import db

class QRCode(db.Model):
  __tablename__ = 'qr_codes'
  
  id: Mapped[int] = mapped_column(db.Integer, primary_key=True)
  hash: Mapped[str] = mapped_column(db.String, unique=True)

  user: Mapped['User'] = relationship('User', back_populates='qr_code')
  scans: Mapped['Scan'] = relationship('Scan', back_populates='qr_code', uselist=True, cascade='all, delete')
