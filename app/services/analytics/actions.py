from api.exceptions import BadRequestException, NotFoundException
from models.qr_code import QRCode
from models.scan import Scan
from datetime import datetime
from db import db

def scan_qr_code(qr_code_id: int, date: datetime):
  qr_code = QRCode.query.filter_by(id=qr_code_id).first()
  if not qr_code: raise NotFoundException

  scan = Scan(qr_code_id=qr_code_id, date=date)
  if not scan: raise BadRequestException

  db.session.add(scan)
  db.session.commit()
