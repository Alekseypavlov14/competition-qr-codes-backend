from services.auth.headers import get_auth_header
from services.qr_code.hash import generate_unique_hash
from services.auth.session import get_user_session_by_token
from api.exceptions import UnauthorizedException, InternalServerException
from models.qr_code import QRCode
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
