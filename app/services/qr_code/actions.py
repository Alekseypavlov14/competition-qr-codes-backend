from services.auth.headers import get_auth_header
from services.qr_code.hash import generate_unique_hash
from services.auth.session import get_user_session_by_token
from api.exceptions import UnauthorizedException, InternalServerException, BadRequestException, NotFoundException
from services.serialization.qr_code import get_qr_code_dict
from services.qr_code.dto import QRCodeDTO
from models.qr_code import QRCode
from models.scan import Scan
from datetime import datetime
from db import db

def create_qr_code(dto: QRCodeDTO):
  token = get_auth_header()
  if not token: raise UnauthorizedException

  session = get_user_session_by_token(token)
  hash = generate_unique_hash()

  qr_code = QRCode(user_id=session.user_id, content=dto.content, hash=hash, date=dto.date)
  if not qr_code: raise InternalServerException

  db.session.add(qr_code)
  db.session.commit()

  return qr_code

def scan_qr_code(hash: str, date: datetime):
  qr_code = QRCode.query.filter_by(hash=hash).first()
  if not qr_code: raise NotFoundException

  scan = Scan(qr_code_id=qr_code.id, date=date)
  if not scan: raise BadRequestException

  db.session.add(scan)
  db.session.commit()

  return qr_code

def delete_qr_code(id: int):
  qr_code_query = QRCode.query.filter_by(id=id)

  qr_code = qr_code_query.first()
  qr_code_dict = get_qr_code_dict(qr_code)

  if not qr_code: raise NotFoundException

  qr_code_query.delete()
  db.session.commit()

  return qr_code_dict
