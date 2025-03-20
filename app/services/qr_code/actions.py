from services.auth.headers import get_auth_header
from services.qr_code.hash import generate_unique_hash
from services.auth.session import get_user_session_by_token
from api.exceptions import UnauthorizedException, InternalServerException, BadRequestException, NotFoundException
from models.qr_code import QRCode
from models.scan import Scan
from datetime import datetime
from db import db

def create_qr_code(content: str):
  token = get_auth_header()
  if not token: raise UnauthorizedException

  session = get_user_session_by_token(token)
  hash = generate_unique_hash()

  qr_code = QRCode(user_id=session.user_id, content=content, hash=hash)
  if not qr_code: raise InternalServerException

  db.session.add(qr_code)
  db.session.commit()

  return qr_code

def scan_qr_code(qr_code_id: int, date: datetime):
  qr_code = QRCode.query.filter_by(id=qr_code_id).first()
  if not qr_code: raise NotFoundException

  scan = Scan(qr_code_id=qr_code_id, date=date)
  if not scan: raise BadRequestException

  db.session.add(scan)
  db.session.commit()
