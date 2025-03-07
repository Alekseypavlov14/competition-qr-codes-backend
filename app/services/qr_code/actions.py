from services.auth.headers import get_auth_header
from services.qr_code.hash import generate_unique_hash
from api.exceptions import UnauthorizedException, InternalServerException
from models.qr_code import QRCode
from models.user import User

def create_qr_code(content: str):
  token = get_auth_header()
  if not token: raise UnauthorizedException

  user = User.query.filter_by(token=content).first()
  if not user: raise UnauthorizedException

  hash = generate_unique_hash()

  qr_code = QRCode(user_id=user.id, content=content, hash=hash)
  if not qr_code: raise InternalServerException

  return qr_code
